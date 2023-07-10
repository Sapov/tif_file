import os
import data
from pyinputplus import inputMenu


class EnterData:
    ''' класс для ввода данных'''

    def __init__(self):
        self.path_dir = str(input("[INFO] Введите путь к каталогу: "))
        self.client = input('Введите имя клиента: ')

    #     '''
    #     Вводим путь проверяем его на существование
    #     Если есть проверяем на сущестование в каталоге TIFF файлов
    #     '''
    #     f = 0
    #     while f == 0:
    #         if os.path.exists(path_dir):
    #             f = 1
    #             os.chdir(path_dir)  # переходим в указанный каталог
    #             lst = os.listdir()  # читаем имена файлов в список
    #             lst = [i for i in lst if i.endswith('.tif') or i.endswith('.tiff')]
    #             if lst:
    #                 return lst
    #             else:
    #                 f = 0
    #                 print('[INFO] Файлов для печати на обнаружено')
    #         else:
    #             print("[INFO] Путь не существует")
    def read_files(self):
        '''Читаем тиф файлы из каталога'''
        os.chdir(self.path_dir)  # переходим в указанный каталог
        lst = os.listdir()  # читаем имена файлов в список
        lst = [i for i in lst if i.endswith('.tif') or i.endswith('.tiff')]
        if lst:
            return lst

    def select_material(self) -> str:
        '''Функция выбора материала для печати'''
        return inputMenu([i for i in data.propertis_material_o], prompt="Выбираем материал для печати: \n", numbered=True)
    def select_type_print(self) -> str:
        '''Функция выбора типа печати'''
        return inputMenu([i for i in data.type_print], prompt="Выберите тип печати: \n", numbered=True)




if __name__ == '__main__':
    a = EnterData()
    a.read_files()
    print(a.__dict__)
    type_print = a.select_type_print()
    print(type_print)
    material = a.select_material()
    print(material)



