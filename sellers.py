from faker import Faker
import random
from database import connection

fake = Faker('id_ID')

kota_ids = [3171, 3172, 3173, 3174, 3175, 3573, 3578, 3471, 3273, 1371, 1375, 6471, 6472, 7371, 5171]


def insert_dummy_data():
    conn = connection()
    cur = conn.cursor()

    try:
        for _ in range(50):
            name = fake.name()
            phone_number = fake.phone_number()
            email = fake.email()
            kota_id = random.choice(kota_ids)

            cur.execute(
                "INSERT INTO sellers (name, phone_number, email, kota_id) VALUES (%s, %s, %s, %s)",
                (name, phone_number, email, kota_id)
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
