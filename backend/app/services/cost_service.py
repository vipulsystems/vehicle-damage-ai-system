from app.repositories.vehicle_repository import get_part_price


def calculate_cost(parts, brand, model):
    total_cost = 0
    breakdown = {}

    for part, count in parts.items():
        price = get_part_price(brand, model, part)

        # 🔥 FIX: convert Decimal → float
        price = float(price) if price else 0.0

        damage_factor = 1.2

        total = price * count * damage_factor

        breakdown[part] = {
            "count": count,
            "price": price,
            "total": total
        }

        total_cost += total

    return total_cost, breakdown