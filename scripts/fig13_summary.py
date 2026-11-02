"""Fig. 25 — Summary normalized comparison across seven metrics."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, save

metrics = ["RMSE", "Energy", "Live", "Delay", "Packets", "Loc.Ratio", "Comm.Range"]
data = {
    "NL2T":      [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
    "ISAC-MAC":  [0.94, 0.74, 0.95, 0.91, 0.94, 0.92, 0.90],
    "ETTOR-RL":  [0.67, 0.67, 0.92, 0.88, 0.93, 0.86, 0.85],
    "BGOR":      [0.66, 0.62, 0.87, 0.86, 0.89, 0.82, 0.82],
    "EERPA":     [0.64, 0.91, 0.93, 0.88, 0.87, 0.85, 0.84],
    "QTRU":      [0.70, 0.78, 0.90, 0.86, 0.89, 0.86, 0.86],
    "DQN-ACMAC": [0.75, 0.50, 0.82, 0.90, 0.95, 0.90, 0.88],
    "AUV-MR3D":  [0.90, 0.57, 0.89, 0.88, 0.91, 0.91, 0.90],
}
fig, ax = plt.subplots(figsize=(14, 7))
x = np.arange(len(metrics)); bar_w = 0.10
for i, m in enumerate(METHODS):
    ax.bar(x + i * bar_w, data[m], bar_w, label=m,
           color=COLORS[m], edgecolor="black")
ax.set_xticks(x + 4 * bar_w); ax.set_xticklabels(metrics, fontsize=9)
ax.set(ylabel="Normalized score (higher is better)", title="Summary performance")
ax.legend(fontsize=7, ncol=4, loc="upper right")
ax.grid(alpha=0.3, axis="y"); ax.set_ylim(0, 1.4)
save(fig, "Fig_13_Summary")
