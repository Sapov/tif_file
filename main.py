from datetime import date
import os
import zipfile
import data
from tqdm import tqdm
import img_file.img_tif
import yandex_disk
from yandex_disk import Yadisk, local_path_yadisk
from pyinputplus import inputMenu
import send_mail
from img_file.img_tif import CheckImage
from calculation import Banner


def write_file_txt(name: str, list_text: str):
    with open(f'{name}_{date.today()}.txt', "w") as file:
        # print(list_text, file=file)
        file.write(list_text)


def arh(list_files: list, material_name: str) -> None:  # add tif to ZIP file
    if os.path.isfile(f'{material_name}_{date.today()}.zip'):
        print('Файл уже существует, архивация пропущена')
    else:
        print("Архивируем файлы:", *list_files)
        for name in tqdm(list_files):
            arh_name = f'{material_name}_{date.today()}.zip'
            new_arh = zipfile.ZipFile(arh_name, "a")
            new_arh.write(name, compress_type=zipfile.ZIP_DEFLATED)
            new_arh.close()


def select_oraganization():
    '''
    Выбор организации для отправки файлов
         '''
    return inputMenu([i for i in data.organisations], prompt='Выбирите организацию куда отправить файлы: \n',
                     numbered=True)


class WorkFile:
    def __init__(self):
        self.path_dir = None  # Путь к директории
        self.lst_tif = None  # список все файлов Tiff (если такие есть)
        self.type_print = None  # Тип печати
        self.material = None  # Тип материала
        self.client = None  # Имя клиента

    def input_path(self: str) -> list[str]:
        '''
        Вводим путь проверяем его на существование
        Если есть проверяем на сущестование в каталоге TIFF файлов
        выводим список тиф файлов
        '''
        f = 0
        while f == 0:
            self.path_dir = str(input("[INFO] Введите путь к каталогу: "))
            # path_dir = '/home/sasha/Загрузки/test/'
            # self.path_dir = '/home/sasha/Загрузки/test/'

            if os.path.exists(self.path_dir):
                f = 1
                os.chdir(self.path_dir)  # переходим в указанный каталог
                lst = os.listdir()  # читаем имена файлов в список
                self.lst_tif = [i for i in lst if i.endswith('.tif') or i.endswith('.tiff')]
                if self.lst_tif:
                    return self.lst_tif
                else:
                    f = 0
                    print('[INFO] Файлов для печати на обнаружено')
            else:
                print("[INFO] Путь не существует")

    def select_type_print(self) -> str:
        '''Функция выбора типа печати'''
        self.type_print = inputMenu([k for k in data.type_print], prompt="Выберите тип печати: \n", numbered=True)

        return self.type_print

    def select_material(self) -> str:
        if self.type_print == 'Широкоформатная печать':
            '''Функция выбора материала для печати'''
            self.material = inputMenu([i for i in data.propertis_material_sirka],
                                      prompt="Выбираем материал ШП  печати: \n",
                                      numbered=True)
            return self.material

        elif self.type_print == 'Интерьерная печать':
            self.material = inputMenu([i for i in data.propertis_material_interierka],
                                      prompt="Выбираем материал интерьерной печати: \n", numbered=True)
            return self.material

        elif self.type_print == 'УФ-Печать':
            self.material = inputMenu([i for i in data.propertis_material_UV],
                                      prompt="Выбираем материал УФ-Печати: \n", numbered=True)
            return self.material

    def input_client(self):
        self.client = input('Введите имя клиента: ')
        return self.client



def main():
    a = WorkFile()
    lst_tif = a.input_path()
    a.input_client()
    type_print = a.select_type_print()
    material = a.select_material()  # выбираем материал

    # _________________________работа с изображением_________________________
    img = CheckImage(type_print, lst_tif, material)
    img.finish_works()
    img.select_fields()
    img.check_resolution()
    # add_border(lst_tif)  # Делаем бордер по контуру всего файла
    # thumbnail(lst_tif) # превьюхи --
    # ----------------------Пишем файл с характеристиками-----------------------
    text_file_name = img.rec_to_file()
    print(img.__dict__)

    arh(lst_tif, material)  # aрхивация
    organizations = select_oraganization()
    # пишем в базу
    # insert_tables(text_file_name, organizations)
    path_save = f'{organizations}/{date.today()}'
    # zip_name = f'{material}_{date.today()}.zip'
    # --------------------------Work in Yandex Disk--------------------------------#
    path_for_yandex_disk = f'{path_save}/{a.client}'  # Путь на яндекс диске для публикации
    Yadisk(path_save).create_folder()  # Создаем папку на yadisk с датой
    Yadisk(path_for_yandex_disk).create_folder()  # # Создаем папку на yadisk с клиентскими файлами
    Yadisk(path_for_yandex_disk).add_yadisk_locate()  # copy files in yadisk
    link = Yadisk(path_for_yandex_disk).add_link_from_folder_yadisk()  # Опубликовал папку получил линк
    # -----------------------------------Work in Mail--------------------------------------#
    os.chdir(f'{yandex_disk.local_path_yadisk}/{path_for_yandex_disk}')  # перехожу в каталог яндекс диска
    with open(text_file_name) as file:  # читаю файл txt
        new_str = file.read()
        send_mail.send_mail(message=f'{new_str} \nCсылка на архив: {link}', subject=material)
    #
    # assert type(self.number_of_pieces('10штбвннерю.tif')) == int, "Возвращает число "
    # assert number_of_pieces('2штбвннерю.tif') == 2, "Возвращает число 2"
    # assert number_of_pieces('тбвннерю.tif') == 1, "Если явно не указано количество *в штуках Возвращает число 1"



if __name__ == "__main__":
    while True:
        main()
