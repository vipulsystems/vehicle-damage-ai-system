from app.services.db_service import get_connection


def get_part_price(brand, model, part):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT price 
        FROM vehicle_parts_pricing
        WHERE brand=%s AND model=%s AND part=%s
    """, (brand, model, part))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result[0] if result else 0