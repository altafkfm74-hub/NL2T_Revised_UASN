"""Reproduce Table eval100: 8 methods x 50 seeds x 10,000 rounds, 95% CI."""
from __future__ import annotations
import os, csv
import numpy as np
from nl2t.env.world import default_world
from nl2t.sim.engine import simulate
from nl2t.baselines import BASELINES
from nl2t.baselines.nl2t_protocol import NL2TProtocol

SEEDS   = 50
ROUNDS  = 10000
NODES   = 100
OUT_CSV = os.path.join("data", "eval100.csv")


def _ci95(v):
    v = np.asarray(v, float)
    return float(v.mean()), float(1.96 * v.std(ddof=1) / np.sqrt(len(v)))


def _one(proto, seed):
    world = default_world(seed=seed, n_nodes=NODES)
    r = simulate(proto, world, duration_h=ROUNDS / 3600.0, seed=seed)
    return dict(
        pdr        = r.pdr,
        rmse_m     = r.mean_loc_error,
        residual_J = r.metrics.final_residual_J,
        delay_s    = r.mean_delay_s,
        j_per_pkt  = r.metrics.energy_per_packet_J,
        overhead   = r.metrics.control_overhead,
    )


def run_method(name, proto_factory):
    runs = [_one(proto_factory(), s) for s in range(SEEDS)]
    out = {"method": name}
    for key in ["pdr", "rmse_m", "residual_J", "delay_s", "j_per_pkt", "overhead"]:
        vals = [r[key] for r in runs]
        out[key], out[key + "_ci"] = _ci95(vals)
    return out


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    rows = [run_method("NL2T", NL2TProtocol)]
    for name, cls in BASELINES.items():
        rows.append(run_method(name, cls))
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"Wrote {OUT_CSV}")
    for r in rows:
        print(f"{r['method']:11s} PDR={r['pdr']:.3f}  "
              f"RMSE={r['rmse_m']:.3f}m  Res={r['residual_J']:.0f}J  "
              f"D={r['delay_s']:.3f}s  J/pkt={r['j_per_pkt']:.2f}  "
              f"OH={r['overhead']:.3f}")
