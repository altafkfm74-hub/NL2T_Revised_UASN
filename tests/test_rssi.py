import numpy as np
from nl2t.core import rssi


def test_rssi_monotone():
    assert rssi.rssi(100.0) > rssi.rssi(1000.0)


def test_roundtrip():
    d = 500.0
    R = rssi.rssi(d)
    assert abs(rssi.range_from_rssi(R) - d) < 1e-6
