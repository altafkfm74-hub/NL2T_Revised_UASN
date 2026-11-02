from nl2t.core import energy


def test_energy_node_positive():
    E = energy.E_node(
        t_state={"active": 10.0, "idle": 5.0, "sleep": 100.0},
        t_mode={"tx": 2.0, "rx": 2.0, "idle": 5.0, "sleep": 100.0},
        t_active=10.0,
    )
    assert E > 0


def test_modem_wake_time():
    t = energy.modem_wake_time()
    assert 0.085 < t < 0.180


def test_state_powers_match_table():
    assert abs(energy.state_power("Active") - 2.06) < 1e-3
    assert abs(energy.state_power("Wait")   - 0.09) < 1e-3
    assert abs(energy.state_power("Sleep")  - 0.004) < 1e-3
