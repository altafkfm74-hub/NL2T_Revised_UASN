"""
Three cross-layer couplings.

    Coupling 1 (Eq. h_coupling):            h(sigma_loc^2) = h0 (1 + kappa_h sigma_loc^2/sigma_ref^2)
    Coupling 2 (Eq. energy_filter_coupling): EKF if S+<h AND S-<h  OR  E_res < E_th_PF, else PF
    Coupling 3 (Eq. residual-wakeup):        if ||z_k - h(x)|| > eta -> C4 wake-up
"""
from __future__ import annotations


def h_coupling(sigma_loc_sq, h0=5.62, kappa_h=0.5, sigma_ref_sq=1.0):
    """Coupling 1."""
    return float(h0 * (1.0 + kappa_h * sigma_loc_sq / max(sigma_ref_sq, 1e-9)))


def adaptive_filter_energy_coupled(S_plus, S_minus, h, E_res, E_th_pf):
    """Coupling 2."""
    if E_res < E_th_pf:
        return "EKF"
    return "EKF" if (S_plus < h and S_minus < h) else "PF"


def residual_wakeup(residual, eta=2.0):
    """Coupling 3."""
    return bool(residual > eta)
