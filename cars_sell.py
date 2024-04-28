from faker import Faker
from datetime import datetime, timedelta
import random

from database import connection


fake = Faker()


def insert_dummy_data():
    conn = connection()
    cur = conn.cursor()

    try:
        for _ in range(250):
            product_id = random.randint(1, 50)
            seller_id = random.randint(1, 50)

            # Generate a random date between January 2024 to March 2024
            start_date = datetime(2024, 1, 1)
            end_date = datetime(2024, 3, 31)
            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            date_post = start_date + timedelta(days=random_number_of_days)

            cur.execute(
                """
                INSERT INTO cars_sell (product_id, seller_id, is_bid, date_post) 
                VALUES (%s, %s, %s, %s)
                """,
                (product_id, seller_id, True, date_post)
            )

        conn.commit()
        print("Data successfully inserted.")
    except Exception as e:
        print("An error occurred:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    insert_dummy_data()
