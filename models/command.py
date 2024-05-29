import time

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
    cursor = conn.cursor()
    return (conn, cursor)


def check_user(telegram_id):
    conn, cursor = connect_to_db()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM client WHERE tg_id::bigint = %s)", (telegram_id,))
    exists = cursor.fetchone()[0]
    if exists:
        return True
    else:
        return False


def add_user(telegram_id, fi):
    try:
        conn, cursor = connect_to_db()
        cursor.execute('INSERT INTO client (fi, tg_id) VALUES (%s, %s)', (fi, telegram_id))
        conn.commit()
        cursor.close()
        print('Запись была успешно добавлена - ', time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))
    except Exception as e:
        print('Error with inserting: ', e)


def add_phone_number(telegram_id, phone_number):
    try:
        conn, cursor = connect_to_db()
        cursor.execute("UPDATE client SET phone_number = %s WHERE tg_id::bigint = %s", (phone_number, telegram_id))
        conn.commit()
        conn.close()
        print(f'Номер телефона для клиента {telegram_id} успешно добавлен - ', time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))

    except Exception as e:
        print('Error: ', e)
