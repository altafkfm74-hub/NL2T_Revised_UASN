"""Fig. 7-8 — Redundancy detection and state transitions."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import save

fig, axs = plt.subplots(1, 2, figsize=(16, 7))
for ax, title in zip(axs, ["(a) All active", "(b) After state transition"]):
    ax.set_xlim(0, 2000); ax.set_ylim(0, 2000); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(title)
    rng = np.random.default_rng(0)
    for _ in range(20):
        x, y = rng.uniform(100, 1900, 2)
        c = (rng.choice(["#00A000", "#FFC400", "#8B0000"], p=[0.3, 0.4, 0.3])
             if "transition" in title else "#00A000")
        ax.scatter(x, y, s=200, color=c, edgecolor="black")
    ax.scatter([1000], [1000], s=800, marker="*", color="red", edgecolor="black")
save(fig, "Fig_07_Topology_Transition")
