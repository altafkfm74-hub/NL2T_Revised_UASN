import numpy as np
from nl2t.core import pf


def test_pf_estimate_shape():
    rng = np.random.default_rng(0)
    particles = rng.normal(0, 1, (100, 6))
    w = np.full(100, 1 / 100)
    est = pf.pf_estimate(particles, w)
    assert est.shape == (6,)
