"""
ISAC-MAC baseline: Duan et al., IEEE IoT-J 2026.
Integrated sensing-communication MAC with dynamic target tracking.
Representative implementation: anchor-first forwarding when target tracking
is active; energy cost reflects MAC scheduling overhead.
"""
from nl2t.sim.protocol import Protocol
from nl2t.baselines._common import shallowest, anchors, max_energy


class ISACMACProtocol(Protocol):
    name = "ISAC-MAC"

    def choose_next_hop(self, i_node, neighbours, params):
        a = anchors(neighbours)
        if a:
            return max_energy(a)
        c = shallowest(neighbours, i_node)
        return max_energy(c)
