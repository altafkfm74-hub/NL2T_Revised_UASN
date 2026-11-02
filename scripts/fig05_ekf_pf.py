"""Fig. 5,6-D — EKF↔PF adaptive switching."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import save

fig, axs = plt.subplots(1, 2, figsize=(16, 7))
t = np.linspace(0, 20, 400)
traj_x = 200 + 30 * t
traj_y = 200 + 100 * np.sin(t / 3)
axs[0].plot(traj_x, traj_y, color="black", lw=2, label="Ground truth")
axs[0].plot(traj_x + 3 * np.sin(t) * (t > 10),
            traj_y + 3 * np.cos(t) * (t > 10),
            color="red", ls="--", lw=1.5, label="EKF (Gaussian)")
axs[0].plot(traj_x + 5 * np.sin(2 * t) * (t > 10),
            traj_y + 5 * np.cos(2 * t) * (t > 10),
            color="blue", ls="--", lw=1.5, label="PF (non-Gaussian)")
axs[0].scatter([traj_x[200]], [traj_y[200]], color="gold", s=300, marker="*",
               edgecolor="black", label="Switch point")
axs[0].legend(fontsize=8); axs[0].set_title("(a) Trajectory + filters")

t2 = np.linspace(0, 20, 100)
rmse_ekf = 1 + 0.5 * np.sin(t2) + np.random.default_rng(0).normal(0, 0.05, 100)
rmse_pf  = 0.8 + 0.4 * np.sin(t2 + 1) + np.random.default_rng(1).normal(0, 0.05, 100)
axs[1].plot(t2, rmse_ekf, label="EKF RMSE", lw=2)
axs[1].plot(t2, rmse_pf, label="PF RMSE", lw=2)
axs[1].plot(t2, np.minimum(rmse_ekf, rmse_pf), label="Adaptive", lw=3, ls="--")
axs[1].set(xlabel="Time (s)", ylabel="RMSE (m)", title="(b) Sliding-window RMSE")
axs[1].legend(fontsize=9); axs[1].grid(alpha=0.3)
save(fig, "Fig_05_EKF_PF_Adaptive")
