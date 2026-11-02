"""Anchor zones."""
from __future__ import annotations
from nl2t.core.anchor import AnchorZone


def make_zones(n_anchors, backups_per_zone=1):
    zones = []
    for i in range(n_anchors):
        backups = [(i + j) % n_anchors for j in range(1, backups_per_zone + 1)]
        zones.append(AnchorZone(primary=i, backups=backups))
    return zones
