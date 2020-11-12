import psycopg2 as pg
from queries import create_table_queries, drop_table_queries


def create_database():

    # Connect to default database
    connection = pg.connect("host=127.0.0.1 dbname=postgres user=student password=student")
    connection.set_session(autocommit=True)
    cursor = connection.cursor()

    # Create database with UTF-8 encoding
    cursor.execute("DROP DATABASE IF EXISTS sparkifydb")
    cursor.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # Close connection to default database
    connection.close()

    # Connect to sparkify database
    connection = pg.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cursor = connection.cursor()

    return connection, cursor


def drop_tables(cursor, connection):
    for query in drop_table_queries:
        cursor.execute(query)
        connection.commit()


def create_tables(cursor, connection):
    for query in create_table_queries:
        cursor.execute(query)
        connection.commit()


def main():

    conn = pg.connect("host=127.0.0.1 dbname=postgres user=postgres password=student")
    conn.set_session(autocommit=True)
    print("DB started!")


    # connection, cursor = create_database()
    # drop_tables(cursor, connection)
    # create_tables(cursor, connection)
    # connection.close()


if __name__ == '__main__':
    main()
