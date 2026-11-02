"""Fig. 3 — Four-state model with C1-C17 and two roles."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from scripts._presentation import save

fig, ax = plt.subplots(figsize=(12, 9))
ax.set_xlim(0, 12); ax.set_ylim(0, 10); ax.axis("off")
positions = {"Active": (2, 7), "Wait": (10, 7), "Midway": (10, 3),
             "Sleep": (2, 3), "Anchor": (6, 8.5), "Backup": (6, 1.5)}
colors = {"Active": "#00A000", "Wait": "#FFC400", "Midway": "#0044CC",
          "Sleep": "#8B0000", "Anchor": "#7A1FA2", "Backup": "#00B3B3"}
for name, (x, y) in positions.items():
    ax.add_patch(FancyBboxPatch((x - 1, y - 0.5), 2, 1,
                                 boxstyle="round,pad=0.15",
                                 fc=colors[name], ec="black", lw=1.5))
    ax.text(x, y, name, ha="center", va="center", fontweight="bold", color="white")

transitions = [
    ("Active","Wait","C2"), ("Wait","Sleep","C3"), ("Sleep","Active","C4"),
    ("Sleep","Midway","C6"), ("Midway","Wait","C7"), ("Active","Sleep","C8"),
    ("Midway","Active","C9"), ("Wait","Active","C10"), ("Midway","Sleep","C11"),
    ("Active","Anchor","C12"), ("Anchor","Active","C13"),
    ("Anchor","Backup","C14"), ("Backup","Anchor","C15"),
    ("Active","Wait","C16"), ("Wait","Active","C17"),
]
for a, b, lbl in transitions:
    x1, y1 = positions[a]; x2, y2 = positions[b]
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2),
                                 arrowstyle="-|>", mutation_scale=18,
                                 lw=1.2, color="black",
                                 connectionstyle="arc3,rad=0.12"))
    ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.2, lbl, fontsize=9,
            fontweight="bold", ha="center",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="black"))
ax.set_title("Four-state model with C1-C17 (Table state-000)", fontsize=12)
save(fig, "Fig_02_State_Machine")
