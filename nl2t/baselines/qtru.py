"""
QTRU baseline: Khoshvaght et al., EAAI 2025.
Q-learning-based tree routing.
Representative implementation: tabular Q updated online, greedy next-hop.
"""
from nl2t.sim.protocol import Protocol
from nl2t.baselines._common import shallowest


class QTRUProtocol(Protocol):
    name = "QTRU"

    def __init__(self):
        self.Q = {}

    def choose_next_hop(self, i_node, neighbours, params):
        cands = shallowest(neighbours, i_node)
        if not cands:
            return None
        def q_value(j):
            key = (i_node.idx, j.idx)
            q = self.Q.get(key, 0.0)
            return q + 0.05 * (i_node.xyz[2] - j.xyz[2]) + 0.02 * j.E
        best = max(cands, key=q_value)
        key = (i_node.idx, best.idx)
        self.Q[key] = self.Q.get(key, 0.0) + 0.1
        return best
