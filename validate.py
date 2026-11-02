"""
Validate the reproduced numbers against the paper's headline claims.
Exit 0 = all PASS.
"""
from __future__ import annotations
import sys, csv, os
from nl2t.core import cusum, energy

TOL = 0.02
results = []


def check(name, got, want, tol=TOL):
    ok = abs(got - want) <= tol * max(abs(want), 1.0)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: got {got:.6g}, want {want:.6g}")
    results.append(ok)


# 1. CUSUM threshold
h = cusum.threshold(P_FA=1e-3, Delta=0.5, alpha=0.3, lam=2.0, sigma=1.0)
check("CUSUM h", h, 5.62)

# 2. State powers from Table energy-table
check("Active power (W)", energy.state_power("Active"), 2.06, tol=0.001)
check("Wait power (W)",   energy.state_power("Wait"),   0.09, tol=0.001)
check("Sleep power (W)",  energy.state_power("Sleep"),  0.004, tol=0.001)

# 3. Headline numbers from Table eval100
csv_path = os.path.join("data", "eval100.csv")
if os.path.exists(csv_path):
    with open(csv_path) as f:
        rows = list(csv.DictReader(f))
    row = next((r for r in rows if r["method"] == "NL2T"), None)
    if row is None:
        print("[SKIP] NL2T row missing in data/eval100.csv")
    else:
        check("NL2T PDR",         float(row["pdr"]),        0.975, tol=0.03)
        check("NL2T RMSE (m)",    float(row["rmse_m"]),     0.511, tol=0.05)
        check("NL2T residual (J)",float(row["residual_J"]), 3479,  tol=0.10)
        check("NL2T delay (s)",   float(row["delay_s"]),    0.462, tol=0.05)
        check("NL2T J/packet",    float(row["j_per_pkt"]),  1.82,  tol=0.10)
        check("NL2T overhead",    float(row["overhead"]),   0.040, tol=0.15)
else:
    print(f"[SKIP] {csv_path} not found - run scripts/exp_eval100.py first")

sys.exit(0 if all(results) else 1)
