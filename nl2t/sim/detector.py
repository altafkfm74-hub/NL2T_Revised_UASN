"""CUSUM event detector wrapper."""
from __future__ import annotations
from nl2t.core import cusum


class Detector:
    def __init__(self, h=5.62, mu_0=0.0, kappa=0.25, c=1.0):
        self.h, self.mu_0, self.kappa, self.c = h, mu_0, kappa, c
        self.S_plus, self.S_minus, self.last_event = 0.0, 0.0, None

    def step(self, R_n):
        self.S_plus, self.S_minus = cusum.update(
            self.S_plus, self.S_minus, R_n,
            mu_0=self.mu_0, kappa=self.kappa, c=self.c)
        ev, direction = cusum.detect(self.S_plus, self.S_minus, self.h)
        self.last_event = direction if ev else None
        return ev, direction
