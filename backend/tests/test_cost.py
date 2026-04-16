from app.services.cost_service import calculate_cost


def test_cost_calculation_basic():
    parts = {"Bumper": 2}

    total_cost, breakdown = calculate_cost(parts, "Honda", "City")

    assert total_cost >= 0
    assert "Bumper" in breakdown
    assert breakdown["Bumper"]["count"] == 2


def test_cost_empty_parts():
    parts = {}

    total_cost, breakdown = calculate_cost(parts, "Honda", "City")

    assert total_cost == 0
    assert breakdown == {}