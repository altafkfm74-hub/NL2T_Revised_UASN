"""
EERPA baseline: Xu et al., IEEE Sensors J. 2025.
Energy-efficient relay selection + power allocation.
Representative implementation: energy-optimal relay among candidates,
power allocation modelled by reweighting the per-hop energy.
"""
from nl2t.sim.protocol import Protocol
from nl2t.baselines._common import shallowest


class EERPAProtocol(Protocol):
    name = "EERPA"

    def choose_next_hop(self, i_node, neighbours, params):
        cands = shallowest(neighbours, i_node)
        if not cands:
            return None
        def score(j):
            d = (i_node.xyz[2] - j.xyz[2]) + 1e-3
            return j.E / d
        return max(cands, key=score)
