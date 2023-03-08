import psycopg2
from config import host, user, password, dn_name


def create_table_postgres():
    try:
        connection = psycopg2.connect(host=host,
                                      user=user,
                                      password=password,
                                      database=dn_name)
        connection.autocommit = True

        # Create Table
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE Files(
                id serial PRIMARY KEY,
                file_name varchar(50) NOT NULL,
                quantity integer,
                material varchar(50) NOT NULL,
                length varchar(50) NOT NULL,
                width varchar(50) NOT NULL,
                dpi integer,
                color_model varchar(50) NOT NULL,
                size varchar(50) NOT NULL,
                price_print money,
                );"""
            )

            print(f'Table created...')


            _________


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')


def insert_data_in_table():
    try:
        connection = psycopg2.connect(host=host,
                                      user=user,
                                      password=password,
                                      database=dn_name)
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO files(first_name, nick_name ) VALUES ('Oleg', 'barracuda');")

            print(f'[INFO] Date created in table...')

            # Выполнение SQL-запроса для вставки данных в таблицу
            # insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
            # cursor.execute(insert_query)


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')

    print(dict_propertis_banner)

# with connection.cursor() as cursor:
#     cursor.execute(
#         'SELECT version();'
#     )
#     print(f'Server version: {cursor.fetchone()}')


# # Insert i  Table
# with connection.cursor() as cursor:
#     cursor.execute(
#         """INSERT INTO files(first_name, nick_name ) VALUES
#         ('Oleg', 'barracuda');"""
#     )
#
#     print(f'[INFO] Date created in table...')


# Get data from Table----------------
# with connection.cursor() as cursor:
#     cursor.execute(
#         """SELECT * FROM files;"""
#     )
#     print(cursor.fetchone())
#
#     print(f'[INFO] Date GET in table...')

# _______________
# try:
#     # Подключение к существующей базе данных
#     connection = psycopg2.connect(user="sasha",
#                                   # пароль, который указали при установке PostgreSQL
#                                   password="111",
#                                   host="192.168.1.105",
#                                   port="5432",
#                                   database="db")
#
#     # Курсор для выполнения операций с базой данных
#     cursor = connection.cursor()
#     # Распечатать сведения о PostgreSQL
#     print("Информация о сервере PostgreSQL")
#     print(connection.get_dsn_parameters(), "\n")
#     # Выполнение SQL-запроса
#     cursor.execute("SELECT version();")
#     # Получить результат
#     record = cursor.fetchone()
#     print("Вы подключены к - ", record, "\n")
#
# except (Exception, Error) as error:
#     print("Ошибка при работе с PostgreSQL", error)
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("Соединение с PostgreSQL закрыто")


create_table_postgres()
