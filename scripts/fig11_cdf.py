"""Fig. 15-17 (c) — CDF of estimation error."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, ax = plt.subplots(figsize=(10, 6))
err = np.linspace(0, 5, 200)
for i, m in enumerate(METHODS):
    scale = 1.5 + 0.15 * i
    cdf = 1 - np.exp(-(err / scale) ** 2)
    ax.plot(err, cdf, color=COLORS[m], ls=STYLES[m], lw=2, label=m)
ax.set(xlabel="Estimation error (m)", ylabel="CDF", title="CDF of estimation error")
ax.legend(fontsize=9); ax.grid(alpha=0.3); ax.set_xlim(0, 5); ax.set_ylim(0, 1.05)
save(fig, "Fig_11_CDF")
