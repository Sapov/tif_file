import psycopg2
from config import host, user, password, dn_name


def create_table_postgres():
    '''
    Добавляем новую таблицу
    '''
    try:
        connection = psycopg2.connect(host=host,
                                      user=user,
                                      password=password,
                                      database=dn_name)
        connection.autocommit = True

        # Create Table
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE NewFiles(
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
                organizations varchar(50) NOT NULL
                );"""
            )

            print(f'Table created...')

        #  _________


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')


def insert_data_in_table(dict_prop_banner: dict):
    '''
    Вставляем данные в таблицу'''

    try:
        connection = psycopg2.connect(host=host,
                                      user=user,
                                      password=password,
                                      database=dn_name)
        connection.autocommit = True

        with connection.cursor() as cursor:
            insert_query = f"""INSERT INTO NewFiles (file_name, quantity, material, length, width,
            dpi, color_model, size, price_print, organizations ) VALUES ('{dict_prop_banner["file_name"]}', {dict_prop_banner["quantity"]}, '{dict_prop_banner["material"]}',
             {dict_prop_banner["length"]}, {dict_prop_banner["width"]}, {dict_prop_banner["dpi"]}, '{dict_prop_banner["color_model"]}', {dict_prop_banner["size"]},
               {dict_prop_banner["price_print"]}, '{dict_prop_banner["organizations"]}')"""
            cursor.execute(insert_query)
            # connection.commit()

            print("запись успешно вставлена")



    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')



def get_postgres():
    ''' Показать всю таблицу'''
    try:
        connection = psycopg2.connect(host=host,
                                      user=user,
                                      password=password,
                                      database=dn_name)
        connection.autocommit = True

        # Create Table
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from NewFiles")
            record = cursor.fetchall()
            # print("Результат", record)
            for i in record:
                print(i)

            print(f'[INFO] Date GET in table...')
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')

def del_postgres(id):
    '''Удаляем строки в таблице'''
    try:
        connection = psycopg2.connect(host=host,
                                      user=user,
                                      password=password,
                                      database=dn_name)
        connection.autocommit = True

        # Create Table
        with connection.cursor() as cursor:
            # Выполнение SQL-запроса для обновления таблицы
            update_query = f'DELETE FROM NewFiles where id = {id}'
            # update_query = """DELETE FROM NewFiles where id = 8"""
            cursor.execute(update_query)
            connection.commit()
            count = cursor.rowcount
            print(count, "Запись успешно удалена")
            # Получить результат
            cursor.execute("SELECT * from NewFiles")
            print("Результат", cursor.fetchall())

            print(f'[INFO] Date GET in table...')
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')

def del_postgres_table():
    ''' Удаляем таблицу NewFiles'''
    try:
        connection = psycopg2.connect(host=host,
                                      user=user,
                                      password=password,
                                      database=dn_name)
        connection.autocommit = True

        # Create Table
        with connection.cursor() as cursor:
            update_query = f'DROP TABLE NewFiles'

            cursor.execute(update_query)
            connection.commit()


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')





get_postgres() # показать записи базы
# Удаление записей по id
# for i in range(16,19):
#     del_postgres(i)

# del_postgres_table()
# create_table_postgres()
