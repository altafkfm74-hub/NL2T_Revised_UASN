from nl2t.env.world import default_world
from nl2t.sim.engine import simulate
from nl2t.baselines import BASELINES
from nl2t.baselines.nl2t_protocol import NL2TProtocol


def test_all_protocols_runnable():
    world = default_world(seed=0, n_nodes=10, anchor_frac=0.3)
    for name, cls in BASELINES.items():
        r = simulate(protocol=cls(), world=world, duration_h=0.05, seed=0)
        assert 0.0 <= r.pdr <= 1.0
    r = simulate(protocol=NL2TProtocol(), world=world, duration_h=0.05, seed=0)
    assert 0.0 <= r.pdr <= 1.0
