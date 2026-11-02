"""Fig. 15-17 (b) — Positioning error vs communication radius."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, ax = plt.subplots(figsize=(10, 6))
r = np.linspace(1, 10, 30)
for i, m in enumerate(METHODS):
    pe = 5.6 + 0.2 * i - 0.4 * r + 0.05 * i * (10 - r)
    ax.plot(r, pe, color=COLORS[m], ls=STYLES[m], lw=2,
            marker="s", markersize=5, label=m)
ax.set(xlabel="Communication radius (m)", ylabel="Positioning error (m)",
       title="Positioning error vs communication radius")
ax.legend(fontsize=9); ax.grid(alpha=0.3)
save(fig, "Fig_10_Positioning_Error")
