import psycopg2
from config import host, user, password, dn_name
from django.db import models
from datetime import datetime


def generate_dict():
    dict_propertis_banner ={}

     # insert in table
    dict_propertis_banner['file_name'] = 'testname'  # имя файла
    dict_propertis_banner['quantity'] = 333  # количество
    dict_propertis_banner['material'] = 'test_material'
    dict_propertis_banner['length'] = 200
    dict_propertis_banner['width'] = 300
    dict_propertis_banner['dpi'] = 72
    dict_propertis_banner['color_model'] = 'RGB'
    dict_propertis_banner['size'] = 1000
    dict_propertis_banner['price_print'] = 202.5 # стоимость
    dict_propertis_banner['organizations'] = 'organizations'  # organizations
    return dict_propertis_banner



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
            
            

            print(f'Table created...')

        #  _________


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')


# def insert_data_in_table(dict_prop_banner: dict):
#     '''
#     Вставляем данные в таблицу'''
#
#     try:
#         connection = psycopg2.connect(host=host,
#                                       user=user,
#                                       password=password,
#                                       database=dn_name)
#         connection.autocommit = True
#
#         with connection.cursor() as cursor:
#             insert_query = f"""INSERT INTO NewFiles (file_name, quantity, material, length, width,
#             dpi, color_model, size, price_print, organizations ) VALUES ('{dict_prop_banner["file_name"]}', {dict_prop_banner["quantity"]}, '{dict_prop_banner["material"]}',
#              {dict_prop_banner["length"]}, {dict_prop_banner["width"]}, {dict_prop_banner["dpi"]}, '{dict_prop_banner["color_model"]}', {dict_prop_banner["size"]},
#                {dict_prop_banner["price_print"]}, '{dict_prop_banner["organizations"]}')"""
#             cursor.execute(insert_query)
#             # connection.commit()
#
#             print("запись успешно вставлена")
#
#
#
#     except Exception as _ex:
#         print("[INFO] Error while working with PostgreSQL", _ex)
#
#     finally:
#         if connection:
#             connection.close()
#             print('[INFO] PostgreSQL connection closed')
#


def insert_data_in_table(dict_prop_banner: dict):
    '''
    Вставляем данные в таблицу FILES_PRODUCT'''

    try:
        connection = psycopg2.connect(host=host,
                                      user=user,
                                      password=password,
                                      database=dn_name)
        connection.autocommit = True

        # )

        with connection.cursor() as cursor:
            # SET TimeZone = 'UTC';
            # SELECT TIME '07:00' AT TIME ZONE 'Australia/Sydney';
            insert_query = f"""INSERT INTO FILES_PRODUCT (quantity, width, length, resolution, color_model, size,
             images, price, created_at, updated_at) VALUES 
            ({dict_prop_banner["quantity"]}, {dict_prop_banner["width"]}, {dict_prop_banner["length"]}, 
            {dict_prop_banner["dpi"]}, '{dict_prop_banner["color_model"]}', {dict_prop_banner["size"]},
             '{dict_prop_banner["file_name"]}', {dict_prop_banner["price_print"]}, {LOCALTIMESTAMP}, {LOCALTIMESTAMP}
            )
            """
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

# get_postgres() # показать записи базы
# Удаление записей по id
# for i in range(1,3):
#     del_postgres(i)

# del_postgres_table()
# create_table_postgres()


#
# if __name__ == '__main__':
#
insert_data_in_table(generate_dict())
