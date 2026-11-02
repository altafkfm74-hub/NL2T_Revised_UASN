"""Fig. 10 — Unified target tracking framework."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from scripts._presentation import save

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14); ax.set_ylim(0, 8); ax.axis("off")
blocks = [
    (1.5, 6, 2.0, 1, "CUSUM\nDetection", "#FFC400"),
    (5.5, 6, 2.0, 1, "Adaptive\nSwitch", "#FF6600"),
    (9.5, 6, 2.5, 1, "Model Select\nCV / CA", "#0044CC"),
    (1.5, 3, 2.0, 1, "EKF\n(Gaussian)",   "#00A000"),
    (5.5, 3, 2.0, 1, "PF\n(Non-Gaussian)","#8B0000"),
    (9.5, 3, 2.5, 1, "State Update\n+ Weights","#7A1FA2"),
    (5.5, 0.5, 2.0, 1, "Tracked Trajectory\nT^(j)","#00B3B3"),
]
for x, y, w, h, label, c in blocks:
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                                 fc=c, ec="black", lw=1.2))
    ax.text(x + w/2, y + h/2, label, ha="center", va="center",
            fontweight="bold", color="white", fontsize=10)
for (x1, y1, x2, y2) in [(3.5,6.5,5.5,6.5), (7.5,6.5,9.5,6.5),
                          (10.5,6,10.5,4), (9.5,3.5,7.5,3.5),
                          (5.5,3.5,3.5,3.5), (6.5,3,6.5,1.5)]:
    ax.add_patch(FancyArrowPatch((x1,y1), (x2,y2), arrowstyle="-|>",
                                 mutation_scale=20, lw=1.5))
save(fig, "Fig_08_Tracking_Framework")
