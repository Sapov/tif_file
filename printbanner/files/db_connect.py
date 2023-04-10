import psycopg2
from .config import host, user, password, dn_name
# from config import host, user, password, dn_name



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


class Databese:
    def __init__(self, path_preview):
        self.path_preview = path_preview
        self.connection = psycopg2.connect(host=host,
                                           user=user,
                                           password=password,
                                           database=dn_name)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def get_bd(self):
        with self.connection:
            self.cursor.execute("SELECT * from FILES_PRODUCT")
            record = self.cursor.fetchall()
            for i in record:
                print(i)

    def create_table_postgres(self):
        '''
        Добавляем новую таблицу
        '''
        with self.connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE NewTest(
                id serial PRIMARY KEY,

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

    def insert_data_in_table(self, dict_prop_banner: dict):
        '''
        Вставляем данные в таблицу FILES_PRODUCT'''

        with self.connection.cursor() as cursor:
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

    def update_last_row(self):
        print(self.path_preview)
        with self.connection:
            self.cursor.execute(
                f'''UPDATE FILES_PRODUCT SET preview_images = '{self.path_preview}' WHERE id = (SELECT max(id) from FILES_PRODUCT);''')

    def insert_preview(self):
        print(self.path_preview)
        with self.connection:
            self.cursor.execute(
                f'''UPDATE FILES_PRODUCT SET preview_images = '{self.path_preview}' WHERE id = (SELECT max(id) from FILES_PRODUCT);''')
            # f''' INSERT INTO FILES_PRODUCT (preview_images) VALUES('{self.path_preview}')''')

