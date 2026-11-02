"""
CV/CA motion models and Eq. adaptive_switch.
"""
from __future__ import annotations
import numpy as np


def F_CV(dt):
    I = np.eye(3)
    return np.block([[I, dt * I], [np.zeros((3, 3)), I]])


def F_CA(dt):
    I, O = np.eye(3), np.zeros((3, 3))
    return np.block([[I, dt * I, 0.5 * dt ** 2 * I],
                     [O, I, dt * I],
                     [O, O, I]])


def select_F(v_prev, dt, threshold_v=2.0):
    """Eq. model_selection."""
    return F_CV(dt) if np.linalg.norm(v_prev) < threshold_v else F_CA(dt)


def adaptive_filter(S_plus, S_minus, h, E_res, E_th_pf):
    """Eq. adaptive_switch + Eq. energy_filter_coupling."""
    if E_res < E_th_pf:
        return "EKF"
    return "EKF" if (S_plus < h and S_minus < h) else "PF"
