"""Fig. 5,6-C — Robust CUSUM detection."""
import numpy as np, matplotlib.pyplot as plt
from nl2t.core import cusum, rssi
from scripts._presentation import save

rng = np.random.default_rng(42)
n = 200
noise = rssi.sample_noise(rng, sigma=1.0, lam=2.0, alpha=0.3, size=n)
event = np.zeros(n); event[130:] = 0.8
R = -60 + noise + event

S_p, S_m = np.zeros(n), np.zeros(n)
Sp, Sm = 0.0, 0.0
for i, r in enumerate(R):
    Sp, Sm = cusum.update(Sp, Sm, r, mu_0=-60, kappa=0.25, c=1.0)
    S_p[i], S_m[i] = Sp, Sm

h = 5.62
fig, axs = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
axs[0].plot(R, lw=1.5); axs[0].axvline(130, color="red", ls="--")
axs[0].set(ylabel="R_n (dBm)", title="(a) RSSI under non-Gaussian noise")
axs[1].plot(S_p, color="red", lw=1.5, label="S_n+")
axs[1].plot(S_m, color="blue", lw=1.5, label="S_n-")
axs[1].axhline(h, color="black", ls=":", label=f"h={h}")
axs[1].set(ylabel="CUSUM statistic"); axs[1].legend(fontsize=9)
axs[2].bar(np.arange(n), (S_p >= h) | (S_m >= h), color="green")
axs[2].set(xlabel="Sample n", ylabel="Event flag", title="(c) Detection")
save(fig, "Fig_04_CUSUM")
