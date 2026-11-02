"""Sensor node with FSM state."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from nl2t.core.fsm import State


@dataclass
class Node:
    idx: int
    xyz: np.ndarray
    E0: float = 10000.0    # 10,000 J initial (Table table1)
    Q_max: int = 50
    E: float = None
    q: int = 0
    state: State = State.ACTIVE
    velocity: np.ndarray = None
    is_anchor: bool = False

    def __post_init__(self):
        if self.E is None:
            self.E = self.E0
        if self.velocity is None:
            self.velocity = np.zeros(3)


def make_nodes(positions, anchor_positions=None):
    nodes = []
    n_anchors = 0 if anchor_positions is None else len(anchor_positions)
    for i, p in enumerate(positions):
        n = Node(idx=i, xyz=np.asarray(p, float))
        if i < n_anchors:
            n.is_anchor = True
            n.state = State.ANCHOR
            n.xyz = np.asarray(anchor_positions[i], float)
        nodes.append(n)
    return nodes
