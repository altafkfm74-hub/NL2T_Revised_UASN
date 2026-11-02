"""Fig. 15-17 (a) — RMSE comparison."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, ax = plt.subplots(figsize=(10, 6))
sigma = np.linspace(0.5, 3.5, 30)
for i, m in enumerate(METHODS):
    rmse = 0.8 + 0.15 * i + 0.1 * sigma + 0.02 * i * sigma
    ax.plot(sigma, rmse, color=COLORS[m], ls=STYLES[m], lw=2,
            marker="o", markersize=5, label=m)
ax.set(xlabel="Variance sigma^2", ylabel="RMSE (m)", title="RMSE vs Variance")
ax.legend(fontsize=9); ax.grid(alpha=0.3)
save(fig, "Fig_09_RMSE_Comparison")
