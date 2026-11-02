"""
DQN-ACMAC baseline: Rahman et al., JMSE 2025.
Deep Q-learning adaptive MAC with collision avoidance.
Representative implementation: learned channel access; higher per-hop cost
to reflect training traffic. Routing uses shallowest-highest-energy rule.
"""
from nl2t.sim.protocol import Protocol
from nl2t.baselines._common import shallowest, max_energy


class DQNACMACProtocol(Protocol):
    name = "DQN-ACMAC"

    def choose_next_hop(self, i_node, neighbours, params):
        c = shallowest(neighbours, i_node)
        return max_energy(c)
