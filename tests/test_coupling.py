from nl2t.core import coupling


def test_h_coupling_increases_with_sigma():
    h_lo = coupling.h_coupling(0.1)
    h_hi = coupling.h_coupling(10.0)
    assert h_hi > h_lo


def test_residual_wakeup():
    assert coupling.residual_wakeup(5.0, eta=2.0) is True
    assert coupling.residual_wakeup(1.0, eta=2.0) is False
