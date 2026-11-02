"""
Four-state FSM with two functional roles — Table state-000 (C1-C17).

States  : Active, Wait, Midway, Sleep, Anchor(role), Backup(role)
Messages:
  C1  Active->Active       stay live, no redundancy
  C2  Active->Wait         redundant (>=2 neighbours)
  C3  Wait->Sleep          idle window expired
  C4  Sleep->Active        CUSUM event wake-up
  C5  Sleep->Sleep         heartbeat-only
  C6  Sleep->Midway        routing-only duty
  C7  Midway->Wait         routing complete
  C8  Active->Sleep        energy low or >=3 redundant
  C9  Midway->Active       localization requested
  C10 Wait->Active         full operation resumed
  C11 Midway->Sleep        routing complete + energy low
  C12 Active->Anchor       promote (Anchor functional role)
  C13 Anchor->Active       release role
  C14 Anchor->Backup       primary demoted (energy rotation)
  C15 Backup->Anchor       primary lost, backup promoted
  C16 Active->Wait         PF energy budget exhausted (Coupling 2)
  C17 Wait->Active         tracking residual > eta (Coupling 3)
"""
from __future__ import annotations
from enum import Enum


class State(Enum):
    ACTIVE = "Active"
    WAIT   = "Wait"
    MIDWAY = "Midway"
    SLEEP  = "Sleep"
    ANCHOR = "Anchor"
    BACKUP = "Backup"


TRANSITIONS = {
    ("Active", "C1"):  State.ACTIVE,
    ("Active", "C2"):  State.WAIT,
    ("Active", "C8"):  State.SLEEP,
    ("Active", "C12"): State.ANCHOR,
    ("Active", "C16"): State.WAIT,
    ("Wait",   "C3"):  State.SLEEP,
    ("Wait",   "C10"): State.ACTIVE,
    ("Wait",   "C17"): State.ACTIVE,
    ("Sleep",  "C4"):  State.ACTIVE,
    ("Sleep",  "C5"):  State.SLEEP,
    ("Sleep",  "C6"):  State.MIDWAY,
    ("Midway", "C7"):  State.WAIT,
    ("Midway", "C9"):  State.ACTIVE,
    ("Midway", "C11"): State.SLEEP,
    ("Anchor", "C13"): State.ACTIVE,
    ("Anchor", "C14"): State.BACKUP,
    ("Backup", "C15"): State.ANCHOR,
}


def transition(current_state, msg):
    key = (current_state.value if isinstance(current_state, State) else current_state, msg)
    return TRANSITIONS.get(key, current_state)


PRIORITY = ["C14", "C15", "C17", "C4", "C16", "C2", "C6"]


def arbitrate(arrivals):
    """Pick highest-priority message among simultaneous arrivals (Fig. ev_scheduler(c))."""
    for m in PRIORITY:
        if m in arrivals:
            return m
    return arrivals[0] if arrivals else None


def decide_transition(state, E_res, E_threshold, redundant=False, pf_budget_exhausted=False,
                      tracking_residual_high=False):
    """Priority-ordered message selection from Table state-000."""
    cur = state.value if isinstance(state, State) else state
    if cur == "Anchor" and pf_budget_exhausted:
        return "C14"
    if cur == "Backup" and (E_res > E_threshold * 2):
        return "C15"
    if tracking_residual_high and cur == "Wait":
        return "C17"
    if E_res < E_threshold or redundant:
        if cur == "Active":  return "C8"
        if cur == "Wait":    return "C3"
        if cur == "Midway":  return "C11"
        return "C5"
    if pf_budget_exhausted and cur == "Active":
        return "C16"
    if cur == "Sleep":   return "C4"
    if cur == "Midway":  return "C9"
    if cur == "Wait":    return "C10"
    return "C1"
