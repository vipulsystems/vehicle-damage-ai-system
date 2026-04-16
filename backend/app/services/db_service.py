import psycopg2
from flask import current_app


def get_connection():
    try:
        conn = psycopg2.connect(
            host=current_app.config["DB_HOST"],
            port=current_app.config["DB_PORT"],
            dbname=current_app.config["DB_NAME"],
            user=current_app.config["DB_USER"],
            password=current_app.config["DB_PASSWORD"]
        )
        return conn
    except Exception as e:
        print("DB Connection Error:", e)
        return None