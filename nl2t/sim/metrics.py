"""Metrics container."""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np


@dataclass
class Metrics:
    delivered: int = 0
    sent: int = 0
    delays_s: list = field(default_factory=list)
    loc_errors_m: list = field(default_factory=list)
    per_delivery_energy_j: list = field(default_factory=list)
    control_msgs: int = 0
    death_times_h: list = field(default_factory=list)
    alive_end: int = 0
    n_start: int = 0
    initial_energy_J: float = 10000.0
    final_residual_J: float = 0.0

    @property
    def pdr(self):         return float(self.delivered / self.sent) if self.sent else 0.0
    @property
    def mean_delay_s(self): return float(np.mean(self.delays_s)) if self.delays_s else 0.0
    @property
    def mean_loc_error(self): return float(np.mean(self.loc_errors_m)) if self.loc_errors_m else 0.0
    @property
    def energy_per_bit_nj(self):
        return float(np.mean(self.per_delivery_energy_j) * 1e9) if self.per_delivery_energy_j else 0.0
    @property
    def fnd_h(self):       return float(min(self.death_times_h)) if self.death_times_h else float("inf")
    @property
    def alive_ratio(self): return self.alive_end / self.n_start if self.n_start else 0.0
    @property
    def energy_per_packet_J(self):
        if not self.per_delivery_energy_j: return 0.0
        return float(np.mean(self.per_delivery_energy_j) * 64 * 8)
    @property
    def control_overhead(self):
        return float(self.control_msgs / self.sent) if self.sent else 0.0
