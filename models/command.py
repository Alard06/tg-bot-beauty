import psycopg2

conn = psycopg2.connect(dbname="tg_bot",
                        user="postgres",
                        password="root",
                        host="localhost",
                        port="5432")


def connect_to_db():
    conn = psycopg2.connect(dbname="tg_bot",
                            user="postgres",
                            password="root",
                            host="localhost",
                            port="5432")

    return conn


def check_user(telegram_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (telegram_id,))
    result = cursor.fetchone()
    if result is not None:
        print(True)
    else:
        print(False)
