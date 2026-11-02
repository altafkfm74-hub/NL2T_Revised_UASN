"""
AUV-MR3D baseline: Xu et al., Ocean Eng. 2025.
Energy-aware 3D AUV-enabled mobile relay.
Representative implementation: prefer AUV-relay positions when available;
fallback shallowest-highest-energy.
"""
from nl2t.sim.protocol import Protocol
from nl2t.baselines._common import shallowest, max_energy


class AUVMR3DProtocol(Protocol):
    name = "AUV-MR3D"

    def choose_next_hop(self, i_node, neighbours, params):
        # prefer mobile-relay-like nodes (mid-column, mid-energy)
        relays = [j for j in neighbours if 20.0 < j.xyz[2] < 80.0]
        if relays:
            return max(relays, key=lambda n: n.E)
        c = shallowest(neighbours, i_node)
        return max_energy(c)
