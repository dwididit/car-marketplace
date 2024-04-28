from datetime import datetime, timedelta
import random

from faker import Faker

from database import connection

fake = Faker()


def insert_dummy_data():
    conn = connection()
    cur = conn.cursor()

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 3, 31)

    try:
        for _ in range(500):
            buyer_id = random.randint(1, 50)
            car_sell_id = random.randint(1, 250)
            first_bid_price = random.randint(90000000, 400000000)

            days_between_dates = (end_date - start_date).days
            random_number_of_days = random.randint(0, days_between_dates)
            first_bid_date = start_date + timedelta(days=random_number_of_days)


            if random.choice([True, False]):
                next_bid_price = first_bid_price + random.randint(100000, 10000000)
                additional_days = random.randint(1, 30)
                next_bid_date = first_bid_date + timedelta(days=additional_days)
            else:
                next_bid_price = None
                next_bid_date = None

            cur.execute("""
                INSERT INTO bids (buyer_id, car_sell_id, first_bid_price, first_bid_date, next_bid_price, next_bid_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (buyer_id, car_sell_id, first_bid_price, first_bid_date, next_bid_price, next_bid_date))

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
