"""Helpers shared by all baselines."""
from __future__ import annotations


def shallowest(neighbours, i_node):
    cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
    return cands


def max_energy(cands):
    return max(cands, key=lambda n: n.E) if cands else None


def anchors(neighbours):
    return [j for j in neighbours if j.is_anchor]
