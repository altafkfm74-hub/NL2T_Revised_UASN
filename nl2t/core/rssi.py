"""
RSSI-based ranging — Eq. (rssi_model) and Eq. (mixture_distribution).

    Eq. rssi_model:          R_n = P_0 - 10*gamma*log10(D_n/D_0) + X_n + s_n
    Eq. mixture_distribution: X_n ~ (1-alpha) N(0,sigma^2) + alpha L(0,lambda)

Path-loss exponent gamma in [1.5, 1.8] (shallow/deep).
"""
from __future__ import annotations
import numpy as np


def rssi(D_n, P0=-60.0, D0=1.0, gamma=1.7, X_n=0.0, s_n=0.0):
    """Eq. rssi_model."""
    D = np.maximum(D_n, 1e-3)
    return P0 - 10.0 * gamma * np.log10(D / D0) + X_n + s_n


def sample_noise(rng, sigma=1.0, lam=2.0, alpha=0.3, size=None):
    """Eq. mixture_distribution."""
    gauss   = rng.normal(0.0, sigma, size=size)
    laplace = rng.laplace(0.0, lam, size=size)
    pick    = rng.random(size=size) < alpha
    return np.where(pick, laplace, gauss)


def range_from_rssi(R_n, P0=-60.0, D0=1.0, gamma=1.7):
    """Invert Eq. rssi_model for D_n."""
    return float(D0 * 10 ** ((P0 - R_n) / (10.0 * gamma)))


def trilaterate(p1, p2, p3, r1, r2, r3):
    """Three-anchor trilateration (2D)."""
    p1, p2, p3 = np.asarray(p1)[:2], np.asarray(p2)[:2], np.asarray(p3)[:2]
    A = 2.0 * np.array([p2 - p1, p3 - p1])
    b = np.array([
        r1 ** 2 - r2 ** 2 + np.dot(p2, p2) - np.dot(p1, p1),
        r1 ** 2 - r3 ** 2 + np.dot(p3, p3) - np.dot(p1, p1),
    ])
    try:
        xy = np.linalg.solve(A, b)
        return float(xy[0]), float(xy[1])
    except np.linalg.LinAlgError:
        return float(p1[0]), float(p1[1])
