"""
BGOR baseline: Wang et al., IEEE TCOM 2025.
Bargaining-game-based opportunistic routing.
Representative implementation: next-hop = weighted sum of energy and depth
gain (Nash-product style, deterministic representative).
"""
from nl2t.sim.protocol import Protocol
from nl2t.baselines._common import shallowest


class BGORProtocol(Protocol):
    name = "BGOR"

    def choose_next_hop(self, i_node, neighbours, params):
        cands = shallowest(neighbours, i_node)
        if not cands:
            return None
        def nash(j):
            depth_gain = i_node.xyz[2] - j.xyz[2]
            return max(depth_gain, 1e-6) * max(j.E, 1e-6)
        return max(cands, key=nash)
