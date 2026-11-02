"""Fig. 18-21 — Comparative performance (4 panels, revised baselines)."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, save

fig, axs = plt.subplots(2, 2, figsize=(16, 12))
panels = [
    ("(a) Residual Energy (J)",     "J",       [3479, 2566, 2308, 2161, 3179, 2723, 1730, 1977]),
    ("(b) Packets to BS (x10^3)",   "packets", [98.5, 94.4, 94.5, 89.1, 86.6, 89.1, 94.5, 91.3]),
    ("(c) Live nodes (out of 100)", "nodes",   [98,   93,   90,   85,   91,   88,   80,   87]),
    ("(d) End-to-end delay (s)",    "s",       [0.462, 0.508, 0.522, 0.536, 0.528, 0.536, 0.513, 0.522]),
]
for ax, (title, ylabel, vals) in zip(axs.flat, panels):
    ax.bar(range(len(METHODS)), vals,
           color=[COLORS[m] for m in METHODS], edgecolor="black")
    ax.set_xticks(range(len(METHODS)))
    ax.set_xticklabels(METHODS, rotation=45, ha="right", fontsize=8)
    ax.set(ylabel=ylabel, title=title); ax.grid(alpha=0.3, axis="y")
save(fig, "Fig_12_Comparative")
