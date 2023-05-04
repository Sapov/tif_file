import sqlite3, datetime
import time
# from prettytable import PrettyTable, from_db_cursor
# from ya_token import DB_NAME

DB_NAME = 'test.db'
TABLE_NAME = 'files_product'


class Database:

    def __init__(self, DB_NAME=DB_NAME, TABLE_NAME='files_product'):
        """

        :type client: object
        """
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()
        self.tabl_name = TABLE_NAME

    def add_table(self):
        with self.connection:
            res = self.cursor.execute(f'''

            CREATE TABLE files_product(
                id INTEGER
            NOT NULL PRIMARY KEY AUTOINCREMENT,
            quantity INTEGER NOT NULL,
            width REAL NOT NULL,
            length REAL NOT NULL,
            resolution INTEGER NOT NULL,
            color_model VARCHAR(10) NOT NULL,
            size REAL NOT NULL,
            price DECIMAL NOT NULL,
            images VARCHAR(100) NOT NULL,
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL,
            Contractor_id BIGINT NOT NULL REFERENCES files_contractor(id) DEFERRABLE INITIALLY DEFERRED,
            material_id BIGINT NOT NULL REFERENCES files_material(id) DEFERRABLE INITIALLY DEFERRED,
            preview_images VARCHAR(100)
            );''')

    def insert_date(self, response: dict):
    # try:
        with self.connection:
            self.cursor.execute(f"""INSERT INTO {self.tabl_name}
                          (quantity, width, length, resolution, color_model, size, price, images, created_at, updated_at, Contractor_id, material_id)
                          VALUES
                          ('{response['quantity']}', '{response['width']}', '
                            {response['length']}', '{response['resolution']}', 
                            '{response['color_model']}', '{response['size']}', '{response['price']}', '{response['images']}', 
                            '{response['created_at']}', '{response['updated_at']}', '{response['Contractor_id']}', '{response['material_id']}' );""")


    def show_table(self):
        '''
        ДОБАВИТЬ РАСЧЕТ БАЛАНСА
        Посмотрень инфо по клиенту
        :return:
        '''
        self.cursor.execute(
            f'''SELECT quantity, width, length, resolution, color_model, size, price, images, created_at FROM 
        {self.tabl_name}  ;''')
        mytable = from_db_cursor(self.cursor)
        print(mytable)


if __name__ == '__main__':
    # Database().show_table()
    Database().add_table()
