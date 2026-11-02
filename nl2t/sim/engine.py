"""Event-driven packet-level simulator."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np

from nl2t.env.world import World, default_world
from nl2t.env.node import make_nodes
from nl2t.env import channel, arq
from nl2t.core.fsm import State
from nl2t.sim.metrics import Metrics
from nl2t.sim.detector import Detector

DEFAULT_PARAMS = dict(
    E_threshold=2000.0,
    dt=1.0,
    drift_sigma=0.02,
    anchor_frac=0.20,
    E_th_pf=1500.0,
)


@dataclass
class SimResult:
    pdr: float
    mean_delay_s: float
    mean_loc_error: float
    energy_per_bit_nj: float
    fnd_h: float
    alive_ratio: float
    metrics: Metrics


def simulate(protocol, world: World = None, duration_h: float = 1.0,
             seed: int = 0, params: dict = None) -> SimResult:
    world  = world  or default_world(seed=seed)
    params = {**DEFAULT_PARAMS, **(params or {})}
    rng    = np.random.default_rng(seed)
    nodes  = make_nodes(world.node_positions, world.anchor_positions)
    m = Metrics(); m.n_start = len(nodes); m.initial_energy_J = 10000.0
    det = Detector(h=5.62)

    n_packets = max(300, 20 * len(nodes))
    P_tx_w, P_rx_w = 2.0, 0.75
    T_pkt = 64 * 8 / 2400.0
    E_c   = 1e-6

    for _ in range(n_packets):
        i = int(rng.integers(0, len(nodes)))
        cur = nodes[i]
        if cur.state == State.SLEEP:
            continue
        hop, delay, energy = 0, 0.0, 0.0
        m.sent += 1
        # Localization error for this node (skip anchors)
        if not cur.is_anchor:
            d = np.linalg.norm(cur.xyz - nodes[0].xyz)
            R = _rssi_with_noise(d, rng)
            loc_error = abs(_range_from(R) - d)
            m.loc_errors_m.append(loc_error)
        else:
            loc_error = 0.0
        # multi-hop delivery
        while hop < 6:
            others = [n for n in nodes if n is not cur]
            nxt = protocol.choose_next_hop(cur, others, params)
            if nxt is None:
                break
            per = channel.link_per(d_m=np.linalg.norm(cur.xyz - nxt.xyz))
            ok, n_tx = arq.transmit(per, rng)
            spent = n_tx * (P_tx_w * T_pkt + P_rx_w * T_pkt + E_c)
            energy += spent
            cur.E = max(cur.E - spent, 0.0)
            delay += np.linalg.norm(cur.xyz - nxt.xyz) / 1500.0 + T_pkt
            m.control_msgs += 1
            if not ok:
                break
            cur = nxt
            hop += 1
            if cur.xyz[2] < 10.0:
                m.delivered += 1
                m.delays_s.append(delay)
                m.per_delivery_energy_j.append(energy / (64 * 8))
                break

    m.alive_end = sum(1 for n in nodes if n.E > 0)
    m.final_residual_J = float(np.mean([n.E for n in nodes]))
    return SimResult(pdr=m.pdr, mean_delay_s=m.mean_delay_s,
                     mean_loc_error=m.mean_loc_error,
                     energy_per_bit_nj=m.energy_per_bit_nj,
                     fnd_h=m.fnd_h, alive_ratio=m.alive_ratio, metrics=m)


def _rssi_with_noise(d, rng, sigma=1.0, lam=2.0, alpha=0.3):
    from nl2t.core.rssi import rssi as _rssi, sample_noise
    return _rssi(d, X_n=float(sample_noise(rng, sigma=sigma, lam=lam,
                                           alpha=alpha, size=1)[0]))

def _range_from(R, P0=-60.0, D0=1.0, gamma=1.7):
    return float(D0 * 10 ** ((P0 - R) / (10.0 * gamma)))
