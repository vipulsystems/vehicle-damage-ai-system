from app.services.db_service import get_connection


def create_user(user_data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users 
        (name, email, password, vehicle_id, phone_number, address, car_brand, car_model)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (
        user_data["name"],
        user_data["email"],
        user_data["password"],
        user_data["vehicle_id"],
        user_data["phone_number"],
        user_data["address"],
        user_data["car_brand"],
        user_data["car_model"]
    ))

    user_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return user_id


def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, email, password, car_brand, car_model 
        FROM users 
        WHERE email=%s
    """, (email,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if not row:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "email": row[2],
        "password": row[3],
        "car_brand": row[4],
        "car_model": row[5]
    }


def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, email, car_brand, car_model
        FROM users
        WHERE id=%s
    """, (user_id,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if not row:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "email": row[2],
        "car_brand": row[3],
        "car_model": row[4]
    }