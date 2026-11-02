"""
Extended Kalman Filter — Eqs. (ekf_predict) ... (ekf_cov_update).
"""
from __future__ import annotations
import numpy as np


def h_measurement(x, anchor):
    p = x[:3]
    return float(np.linalg.norm(p - anchor))


def H_jacobian(x, anchor):
    p = x[:3]
    d = p - anchor
    r = max(np.linalg.norm(d), 1e-9)
    return np.concatenate([d / r, np.zeros(3)])


def ekf_predict(x, P, F, Q):
    return F @ x, F @ P @ F.T + Q


def ekf_update(x_pred, P_pred, z, anchor, R):
    H = H_jacobian(x_pred, anchor).reshape(1, -1)
    h = h_measurement(x_pred, anchor)
    S = H @ P_pred @ H.T + R
    K = P_pred @ H.T @ np.linalg.inv(S)
    x_new = x_pred + (K @ (z - h)).flatten()
    I = np.eye(P_pred.shape[0])
    P_new = (I - K @ H) @ P_pred
    return x_new, 0.5 * (P_new + P_new.T)
