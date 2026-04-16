from app.services.db_service import get_connection
import json


def save_report(user_id, image_path, parts, total_cost):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO damage_reports 
        (user_id, image_path, detected_parts, total_cost)
        VALUES (%s, %s, %s, %s)
    """, (
        user_id,
        image_path,
        json.dumps(parts),   # JSONB storage
        total_cost
    ))

    conn.commit()

    cursor.close()
    conn.close()


def get_reports_by_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, image_path, detected_parts, total_cost, created_at
        FROM damage_reports
        WHERE user_id=%s
        ORDER BY created_at DESC
    """, (user_id,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    reports = []

    for row in rows:
        reports.append({
            "id": row[0],
            "image_path": row[1],
            "detected_parts": row[2],  # already JSONB
            "total_cost": row[3],
            "created_at": str(row[4])
        })

    return reports