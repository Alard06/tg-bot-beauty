import psycopg2

import executes


def create_table(cursor, conn):
    cursor.execute(executes.master)
    cursor.execute(executes.client)
    cursor.execute(executes.service)
    cursor.execute(executes.appointments)

    conn.commit()


def show_name_tables(cursor, conn):
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")

    # Вывод результатов
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])


def main():
    conn = psycopg2.connect(dbname="tg_bot",
                            user="postgres",
                            password="root",
                            host="localhost",
                            port="5432")

    cursor = conn.cursor()
    create_table(cursor, conn)
    show_name_tables(cursor, conn)


if __name__ == "__main__":
    main()
