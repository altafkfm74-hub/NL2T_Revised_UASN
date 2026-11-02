"""World container and default deployment (Table table1)."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class World:
    region_xyz: tuple = (2000.0, 2000.0, 100.0)
    n_nodes: int = 100
    seed: int = 0
    sink_xyz: tuple = None
    node_positions: np.ndarray = None
    anchor_positions: np.ndarray = None


def default_world(seed: int = 0, n_nodes: int = 100, anchor_frac: float = 0.20) -> World:
    rng = np.random.default_rng(seed)
    W, H, D = 2000.0, 2000.0, 100.0
    pos = np.column_stack([
        rng.uniform(0, W, n_nodes),
        rng.uniform(0, H, n_nodes),
        rng.uniform(0.0, D, n_nodes),
    ])
    n_anchors = max(3, int(round(anchor_frac * n_nodes)))
    anchor_pos = np.column_stack([
        rng.uniform(0, W, n_anchors),
        rng.uniform(0, H, n_anchors),
        np.full(n_anchors, D * 0.5),
    ])
    return World(region_xyz=(W, H, D), n_nodes=n_nodes, seed=seed,
                 sink_xyz=(W / 2, H / 2, 0.0),
                 node_positions=pos, anchor_positions=anchor_pos)
