"""Fig. 1 — End-to-end communication scenario."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
rng = np.random.default_rng(0)
for ax, title in zip(axs, ["(a) Surface + AUV", "(b) Anchor zones", "(c) Multi-hop to sink"]):
    ax.set_facecolor("#0A2842"); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(0, 2000); ax.set_ylim(0, 2000)
    for _ in range(30):
        ax.scatter(rng.uniform(50, 1950), rng.uniform(50, 1950), s=30,
                   color="#2ECC71", edgecolor="black")
    ax.scatter([1000], [1000], s=500, marker="*",
               color="#FF0000", edgecolor="black", label="Sink")
    ax.set_title(title, color="white")
    ax.legend(fontsize=8, labelcolor="white", facecolor="#0A2842")
save(fig, "Fig_01_Scenario")
