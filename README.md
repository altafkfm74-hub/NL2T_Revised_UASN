# NL2T_Revised_UASN

Reference implementation accompanying the paper:

> A. Hussain, S. Li, M. Jamjoom, Z. Ullah, A. H. Farhan,
> "NL2T: Co-Optimizing Localization Accuracy and Energy Efficiency for
> Adaptive Mobile Target Tracking in Underwater Acoustic Sensor Networks,"
> 2026 (Revision R1).

This is the **revised** package: it implements the 17-message control table
(C1-C17), the three cross-layer couplings, and the seven baselines from the
revised manuscript (ISAC-MAC, ETTOR-RL, BGOR, EERPA, QTRU, DQN-ACMAC,
AUV-MR3D). It reproduces every headline number in the abstract and
Table `eval100`.

## Repository layout

| Part | Module              | Purpose                                                              |
|------|---------------------|----------------------------------------------------------------------|
| I    | `nl2t.core`         | Every equation of Section III (RSSI, CUSUM, EKF, PF, energy, couplings) |
| II   | `nl2t.env`          | World, anchors, four-state FSM, acoustic channel, ARQ                |
| III  | `nl2t.sim`          | Packet-level event-driven simulator + metrics + CUSUM detector       |
| IV   | `nl2t.baselines`    | 8 protocols: NL2T + 7 new baselines (ISAC-MAC ... AUV-MR3D)          |
| V    | `scripts/`          | One script per Section IV / Table eval100                            |

## Install

```bash
pip install -r requirements.txt
```

## 30-second demo

```python
from nl2t.env.world import default_world
from nl2t.sim.engine import simulate
from nl2t.baselines.nl2t_protocol import NL2TProtocol

world = default_world(seed=0, n_nodes=100)
r = simulate(protocol=NL2TProtocol(), world=world, duration_h=1.0, seed=0)
print(f"PDR={r.pdr:.3f}  loc_err={r.mean_loc_error:.3f}m  "
      f"E/bit={r.energy_per_bit_nj:.0f}nJ  alive={r.alive_ratio:.2f}")
```

## Reproduce Table eval100 (all eight methods, 50 seeds, 95% CI)

```bash
python scripts/exp_eval100.py
```

## Reproduce every figure

```bash
python scripts/run_all_figures.py
```

## Validate headline numbers

```bash
python validate.py
# expected: all PASS, exit code 0
```

## Tests

```bash
pytest tests/ -q
```

## Version

v1.1-r1 (Revision 1). Concept DOI: 10.5281/zenodo.23611182.
