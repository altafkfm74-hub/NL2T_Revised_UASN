# Changelog

## [1.1.0] - 2026 (Revision R1)
### Changed
- Replaced the seven old baselines with the seven new ones (ISAC-MAC,
  ETTOR-RL, BGOR, EERPA, QTRU, DQN-ACMAC, AUV-MR3D).
- Expanded the FSM from C1-C13 to C1-C17 (adds Backup role C14-C15 and
  scheduling-side couplings C16-C17), matching Table `state-000`.
- Reworked energy parameters to Table `energy-table` (watts per component).
- Updated headline targets to PDR 0.975, RMSE 0.511 m, residual 3479 J,
  delay 0.462 s, 1.82 J/packet, overhead 0.040.
- Added `validate.py` with PASS/FAIL checks for every headline number.

## [1.0.0] - 2026
- Initial public release.
