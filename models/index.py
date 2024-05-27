import psycopg2


class Database:
    """База данных"""

    conn = psycopg2.connect(dbname="tg_bot",
                            user="postgres",
                            password="root",
                            host="localhost",
                            port="5432")

    cursor = conn.cursor()
def create_table():



def main():
    pass


if __name__ == "__main__":
    main()
