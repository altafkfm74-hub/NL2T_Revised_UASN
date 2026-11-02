"""Presentation helpers."""
from __future__ import annotations
import os
import numpy as np
import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt

METHODS = ["NL2T", "ISAC-MAC", "ETTOR-RL", "BGOR", "EERPA", "QTRU", "DQN-ACMAC", "AUV-MR3D"]

COLORS = {
    "NL2T":      "#FF0000",
    "ISAC-MAC":  "#0044CC",
    "ETTOR-RL":  "#00A000",
    "BGOR":      "#7A1FA2",
    "EERPA":     "#FFC400",
    "QTRU":      "#00B3B3",
    "DQN-ACMAC": "#FF1493",
    "AUV-MR3D":  "#FF6600",
}

STYLES = {
    "NL2T":      "-",
    "ISAC-MAC":  (0, (6, 2)),
    "ETTOR-RL":  (0, (4, 1, 1, 1)),
    "BGOR":      (0, (7, 2, 2, 2)),
    "EERPA":     (0, (2, 1)),
    "QTRU":      (0, (1, 1)),
    "DQN-ACMAC": (0, (3, 1, 1, 1, 1, 1)),
    "AUV-MR3D":  (0, (5, 2, 1, 2)),
}

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Times New Roman"],
    "font.weight": "bold", "axes.labelweight": "bold",
    "axes.titleweight": "bold", "axes.linewidth": 1.4,
    "pdf.fonttype": 42, "ps.fonttype": 42, "savefig.dpi": 600,
    "xtick.direction": "in", "ytick.direction": "in",
})


def save(fig, name):
    os.makedirs("figures", exist_ok=True)
    path = os.path.join("figures", name + ".pdf")
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved " + path)
