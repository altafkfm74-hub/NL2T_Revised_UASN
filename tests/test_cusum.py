from nl2t.core import cusum


def test_threshold_value():
    h = cusum.threshold(P_FA=1e-3, Delta=0.5, alpha=0.3, lam=2.0, sigma=1.0)
    assert abs(h - 5.6166) < 0.01


def test_robust_score():
    assert cusum.robust_score(0.5, c=1.0) == 0.5
    assert cusum.robust_score(5.0, c=1.0) == 1.0
    assert cusum.robust_score(-5.0, c=1.0) == -1.0
