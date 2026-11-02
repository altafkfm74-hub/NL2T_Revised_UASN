"""ARQ transmission with cap."""
from __future__ import annotations
import numpy as np


def transmit(per, rng, max_tx=4):
    for k in range(1, max_tx + 1):
        if rng.random() > per:
            return True, k
    return False, max_tx


def expected_n_tx(per, cap=1e6):
    p = min(max(float(per), 0.0), 1.0 - 1e-12)
    return float(min(1.0 / (1.0 - p), cap))
