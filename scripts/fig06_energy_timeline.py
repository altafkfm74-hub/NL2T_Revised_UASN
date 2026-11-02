"""Fig. 5,6-F — Energy timeline for a single node."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import save

fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
cycles = np.arange(50)
state = np.where(cycles < 10, 0, np.where(cycles < 25, 1, np.where(cycles < 40, 2, 3)))
labels = ["Active", "Wait", "Midway", "Sleep"]
colors = ["#00A000", "#FFC400", "#0044CC", "#8B0000"]
axs[0].scatter(cycles, state, c=[colors[s] for s in state], s=80, edgecolor="black")
axs[0].set_yticks([0, 1, 2, 3]); axs[0].set_yticklabels(labels)
axs[0].set(ylabel="State", title="(a) State timeline")

energy = 10000.0 * np.exp(-0.05 * cycles)
cum = 10000.0 - energy
axs[1].plot(cycles, cum,   color="red",  lw=2, label="Cumulative energy (J)")
axs[1].plot(cycles, energy,color="teal", ls="--", lw=2, label="Residual energy (J)")
axs[1].set(xlabel="Cycle", ylabel="Energy (J)", title="(b) Energy profile")
axs[1].legend(fontsize=9); axs[1].grid(alpha=0.3)
save(fig, "Fig_06_Energy_Timeline")
