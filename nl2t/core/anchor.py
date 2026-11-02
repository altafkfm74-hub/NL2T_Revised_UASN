"""
Anchor fault-tolerance and rotation — Eq. (anchor_set) ... (anchor_rotation).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class AnchorZone:
    primary: int
    backups: List[int] = field(default_factory=list)
    heartbeat_received: bool = True


def heartbeat(H_received, T_heartbeat=1.0, last_heartbeat_t=0.0, now_t=0.0):
    """Eq. heartbeat."""
    return 1 if (now_t - last_heartbeat_t) <= T_heartbeat and H_received else 0


def failover(zone: AnchorZone, heartbeat_lost_rounds, tau_fail=3):
    """Eq. failure_recovery."""
    if heartbeat_lost_rounds >= tau_fail and zone.backups:
        new_primary = zone.backups.pop(0)
        zone.backups.append(zone.primary)
        zone.primary = new_primary
    return zone


def rotate_on_energy(zone: AnchorZone, energies: dict, E_threshold_anchor=2000.0):
    """Eq. anchor_rotation."""
    if energies.get(zone.primary, 0.0) < E_threshold_anchor and zone.backups:
        best = max(zone.backups, key=lambda a: energies.get(a, 0.0))
        zone.backups.remove(best)
        zone.backups.append(zone.primary)
        zone.primary = best
    return zone
