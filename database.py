import psycopg2


def connection():
    db_params = {
        "dbname": "car_marketplace",
        "user": "postgres",
        "password": "postgres",
        "host": "localhost"
    }

    conn = psycopg2.connect(**db_params)
    return conn
