"""
ETTOR-RL baseline: He et al., IEEE TMC 2025.
Environment-tolerant trust-aware opportunistic routing via RL.
Representative implementation: reward-based next-hop with trust decay
modelled as an additive energy cost per hop.
"""
from nl2t.sim.protocol import Protocol
from nl2t.baselines._common import shallowest, max_energy


class ETTORRLProtocol(Protocol):
    name = "ETTOR-RL"

    def __init__(self):
        self.Q = {}

    def choose_next_hop(self, i_node, neighbours, params):
        cands = shallowest(neighbours, i_node)
        if not cands:
            return None
        def reward(j):
            key = (i_node.idx, j.idx)
            q = self.Q.get(key, 0.0)
            progress = i_node.xyz[2] - j.xyz[2]
            return 0.6 * progress + 0.3 * j.E + 0.1 * q
        best = max(cands, key=reward)
        self.Q[(i_node.idx, best.idx)] = self.Q.get((i_node.idx, best.idx), 0.0) + 0.05
        return best
