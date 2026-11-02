import numpy as np
from nl2t.core import ekf, tracker


def test_ekf_predict_dims():
    F = tracker.F_CV(1.0)
    Q = 0.1 * np.eye(6)
    x, P = np.zeros(6), np.eye(6)
    xp, Pp = ekf.ekf_predict(x, P, F, Q)
    assert xp.shape == (6,) and Pp.shape == (6, 6)
