"""Fig. 5-6 — Trilateration + RSSI path-loss."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import save

fig, axs = plt.subplots(1, 2, figsize=(16, 7))
axs[0].set_xlim(0, 100); axs[0].set_ylim(0, 100)
anchors = [(20, 20), (80, 20), (50, 80)]
for i, (ax, ay) in enumerate(anchors):
    axs[0].scatter(ax, ay, s=200, marker="^", color=["red","blue","green"][i],
                   edgecolor="black", label=f"AN{i+1}")
    axs[0].add_patch(plt.Circle((ax, ay), 40, fill=False,
                                 ec=["red","blue","green"][i], ls="--", lw=1.2))
axs[0].scatter([50], [40], s=200, marker="*", color="gold",
               edgecolor="black", label="Est.")
axs[0].legend(fontsize=9); axs[0].set_title("(a) Trilateration")

D = np.linspace(1, 2000, 100)
for gamma in [1.5, 1.7, 1.8]:
    R = -60 - 10 * gamma * np.log10(D)
    axs[1].plot(D, R, lw=2, label=f"gamma={gamma}")
axs[1].set(xlabel="Distance D_n (m)", ylabel="RSSI R_n (dBm)",
           title="(b) RSSI path-loss model")
axs[1].legend(fontsize=9); axs[1].grid(alpha=0.3)
save(fig, "Fig_03_RSSI_Ranging")
