from nl2t.core import fsm


def test_c_table_complete():
    # Every C1..C17 has at least one entry in TRANSITIONS.
    msgs = {k[1] for k in fsm.TRANSITIONS.keys()}
    assert set(f"C{i}" for i in range(1, 18)) <= msgs


def test_active_to_wait():
    assert fsm.transition(fsm.State.ACTIVE, "C2") == fsm.State.WAIT


def test_anchor_backup_rotation():
    assert fsm.transition(fsm.State.ANCHOR, "C14") == fsm.State.BACKUP
    assert fsm.transition(fsm.State.BACKUP, "C15") == fsm.State.ANCHOR
