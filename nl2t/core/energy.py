"""
Energy model — Eqs. (energy_discrete) ... (transition_energy).

Component power levels (W) reproduce Table energy-table:

    MP active 0.05, MP idle 0.04, MP sleep 0.003
    RL tx 2.00, RL rx 0.75, RL idle 0.05, RL sleep 0.001
    SC active 0.01
    Wake 1.5
"""
from __future__ import annotations
import numpy as np

POWER = {
    "MP": {"active": 0.05, "idle": 0.04, "sleep": 0.003},
    "RL": {"tx": 2.00, "rx": 0.75, "idle": 0.05, "sleep": 0.001},
    "SC": {"active": 0.01},
}
P_wake = 1.5

STATE_MODES = {
    "Active": {"MP": "active", "RL": "tx",   "SC": "active"},
    "Wait":   {"MP": "idle",   "RL": "idle", "SC": None},
    "Midway": {"MP": "active", "RL": "idle", "SC": None},
    "Sleep":  {"MP": "sleep",  "RL": "sleep","SC": None},
}


def state_power(state):
    """Sum of component powers in a given four-state value (W)."""
    modes = STATE_MODES[state]
    return float(sum(POWER[c][m] for c, m in modes.items() if m is not None))


def energy_discrete(power_series, dt):
    """Eq. energy_discrete (trapezoid over piecewise-constant power)."""
    p = np.asarray(power_series, dtype=float)
    return float(np.sum(0.5 * (p[:-1] + p[1:]) * dt))


def E_MP(t_state):
    """Eq. energy_mp."""
    return float(sum(POWER["MP"][s] * t_state.get(s, 0.0) for s in POWER["MP"]))


def E_RL(t_mode):
    """Eq. energy_rl."""
    return float(sum(POWER["RL"][m] * t_mode.get(m, 0.0) for m in POWER["RL"]))


def E_SC(t_active):
    """Eq. energy_sc."""
    return float(POWER["SC"]["active"] * t_active)


def E_node(t_state, t_mode, t_active):
    """Eq. energy_total_corrected."""
    return E_MP(t_state) + E_RL(t_mode) + E_SC(t_active)


def t_tx(L_bits, B_rate_bps):
    """Eq. tx_duration: t_tx = L_packet / B_rate."""
    return float(L_bits / max(B_rate_bps, 1e-9))


def modem_wake_time(hw_init=0.075, sync=0.015, calib=0.035, tx_ready=0.008):
    """Eq. modem_wakeup / modem_wakeup_range (default 133 ms)."""
    return hw_init + sync + calib + tx_ready


def E_transition(t_wake):
    """Eq. transition_energy."""
    return float(P_wake * t_wake)
