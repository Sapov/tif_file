from datetime import date
import PIL
from PIL import Image
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


def color_mode(file_name: str) -> str:
    Image.MAX_IMAGE_PIXELS = None

    try:
        with Image.open(file_name) as img:
            mode = img.mode
            if mode == 'CMYK':

                return mode
            else:
                print("Цветовая модель не соответствует требованиям, нужно перевести в CMYK")
                return mode
    except PIL.UnidentifiedImageError:
        print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
            Решение: Photoshop / слои / выполнить сведение''')
        return mode


def size_file(name_file: str) -> float:
    # Размер в МБ
    file_stat = os.stat(name_file)
    return round(file_stat.st_size / (1024 * 1024), 2)


def write_file_txt(name: str, list_text: str):
    with open(f'{name}_{date.today()}.txt', "w") as file:
        # print(list_text, file=file)
        file.write(list_text)


def calculation(width, length, material: str) -> float:
    price_material = data.propertis_material.get(material)[0]
    return round(width * length * price_material, 2)


def calculation_for_client(width, length, material: str) -> float:
    price_material = data.propertis_material.get(material)[3]
    return round(width * length * price_material, 2)


def arh(list_files: list, material_name: str):  # add tif to ZIP file
    if os.path.isfile(f'{material_name}_{date.today()}.zip'):
        print('Файл уже существует, архивация пропущена')
    else:
        print("Архивируем файлы:", *list_files)
        for name in tqdm(list_files):
            new_arh = zipfile.ZipFile(f'{material_name}_{date.today()}.zip', "a")
            new_arh.write(name, compress_type=zipfile.ZIP_DEFLATED)
            new_arh.close()


def select_oraganization():
    '''
    Выбор организации для отправки файлов
         '''
    return inputMenu([i for i in data.organisations], prompt='Выбирите организацию куда отправить файлы: \n',
                     numbered=True)


def number_of_pieces(file_name_in_list: str) -> int:
    '''
    ищем количество в имени файла указываеться после шт
    не покрыта тестами
    '''
    file_name_in_list = file_name_in_list.lower()
    if 'шт' in file_name_in_list:
        quantity_in_name_file = file_name_in_list[:file_name_in_list.find('шт')]
        num = ""
        for i in range(file_name_in_list.find('шт') - 1, -1, -1):
            # print(file_name[i])
            if file_name_in_list[i].isdigit():
                num += str(file_name_in_list[i])
                num = num[::-1]
        return int(num)
    else:
        return 1


# запись в текстовый файл
def rec_to_file(text_file_name: str, lst_tif: list, material):
    itog = 0
    dict_propertis_banner = {}

    with open(text_file_name, "w") as file:
        for i in range(len(lst_tif)):
            w_l_dpi = img_file.img_tif.check_tiff(lst_tif[i])
            assert type(img_file.img_tif.check_tiff(lst_tif[i])) == tuple, 'Ожидаем кортеж'
            P = img_file.img_tif.perimetr(w_l_dpi[0], w_l_dpi[1])  # периметр файла

            file_name = f'File # {i + 1}: {lst_tif[i]}'
            quantity = int(number_of_pieces(lst_tif[i]))
            quantity_print = f'Количество: {quantity} шт.'
            length_width = f'Ширина: {w_l_dpi[0]} см\nДлина: {w_l_dpi[1]} см\nРазрешение: {w_l_dpi[2]} dpi'
            color_model = f'Цветовая модель: {color_mode(lst_tif[i])}'
            size = f'Размер: {size_file(lst_tif[i])} Мб'
            price_one = calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, material)
            square_unit = (w_l_dpi[0] * w_l_dpi[
                1]) / 10000  # площадь печати одной штуки (см приводим к метрам  / 10 000
            square = f'Площадь печати {round(square_unit * quantity, 2)} м2'  # вся площадь печати
            price = price_one * quantity
            price_print = f'Стоимость: {price_one * quantity} руб.\n '
            itog = itog + price
            file.write(
                f'{file_name}\n{quantity_print}\n{length_width}\n{square}\n{color_model}\n{size}\n{price_print}\n')
            file.write("-" * 40 + "\n")

        file.write(f'Итого: {round(itog, 2)} руб.\n')
        print(f'Итого стоимость печати: {round(itog, 2)} руб.')


def file_sale(file_s: str, lst_tif=None):
    itog = 0
    with open(file_s, "w") as file:
        for i in range(len(lst_tif)):
            w_l_dpi = img_file.img_tif.check_tiff(lst_tif[i])
            assert type(img_file.img_tif.check_tiff(lst_tif[i])) == tuple, 'Ожидаем кортеж'
            file_name = f'File # {i + 1}: {lst_tif[i]}'
            quantity = int(number_of_pieces(lst_tif[i]))
            quantity_print = f'Количество: {quantity} шт.'
            length_width = f'Ширина: {w_l_dpi[0]} см\nДлина: {w_l_dpi[1]} см\nРазрешение: {w_l_dpi[2]} dpi'
            square_unit = Banner(w_l_dpi[0], w_l_dpi[1]).square()  # площадь печати
            # square_unit = (w_l_dpi[0] * w_l_dpi[
            #     1]) / 10000  # площадь печати одной штуки (см приводим к метрам  / 10 000
            square = f'Площадь печати {round(square_unit * quantity, 2)} м2'  # вся площадь печати
            color_model = f'Цветовая модель: {color_mode(lst_tif[i])}'
            size = f'Размер: {size_file(lst_tif[i])} Мб'
            price_one = calculation_for_client(w_l_dpi[0] / 100, w_l_dpi[1] / 100,
                                               material)  # считаем стоимость для заказчика
            price = price_one * quantity
            price_print = f'Стоимость: {price_one * quantity} руб.\n '
            itog = itog + price
            file.write(
                f'{file_name}\n{quantity_print}\n{length_width}\n{square}\n{color_model}\n{size}\n{price_print}\n')
            file.write("-" * 40 + "\n")

        file.write(f'Итого: {round(itog, 2)} руб.\n')
        print(f'Итого продажа: {round(itog, 2)} руб.')


class WorkFile:
    def __init__(self):
        self.path_dir = None  # Путь к директории
        self.lst_tif = None  # список все файлов Tiff (если такие есть)
        self.type_print = None  # Тип печати
        self.material = None  # Тип материала
        self.client = None  # Имя клиента
        self.finish_work = None  # финишная обработка
        self.fields = None  # Поля материала

    def input_path(self: str) -> list[str]:
        '''
        Вводим путь проверяем его на существование
        Если есть проверяем на сущестование в каталоге TIFF файлов
        выводим список тиф файлов
        '''
        f = 0
        while f == 0:
            # path_dir = str(input("[INFO] Введите путь к каталогу: "))
            # path_dir = '/home/sasha/Загрузки/test/'
            self.path_dir = '/home/sasha/Загрузки/test/'

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
        '''Функция выбора материала для печати'''
        if self.type_print == 'Широкоформатная печать':
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

    def finish_works(self):
        if "Баннер" in self.material:
            self.finish_work = inputMenu([i for i in data.finishka],
                                         prompt="Финишная обработка баннера: \n", numbered=True)
            return self.finish_work

    def select_fields(self):
        if "Баннер" or "Холст" in self.material:
            self.fields = inputMenu([i for i in data.fields],
                                    prompt="Выбор полей: \n", numbered=True)
            return self.fields

def main():
    a = WorkFile()
    lst_tif = a.input_path()
    type_print = a.select_type_print()
    a.input_client()
    material = a.select_material()  # выбираем материал
    a.finish_works()
    a.select_fields()
    print(a.__dict__)

    #_________________________работа с изображением_________________________
    img = CheckImage(type_print, lst_tif, material)
    img.check_resolution()
    print(img.__dict__)
    # add_border(lst_tif)  # Делаем бордер по контуру всего файла
    # thumbnail(lst_tif) # превьюхи --
    #----------------------Пишем файл с характеристиками-----------------------
    text_file_name = f'{material}_for_print_{date.today()}.txt'
    rec_to_file(text_file_name, lst_tif, material)

    arh(lst_tif, material)  # aрхивация
    organizations = select_oraganization()
    # пишем в базу
    # insert_tables(text_file_name, organizations)
    path_save = f'{organizations}/{date.today()}'
    zip_name = f'{material}_{date.today()}.zip'
    # --------------------------Work in Yandex Disk--------------------------------#
    path_for_yandex_disk = f'{path_save}/{client}'  # Путь на яндекс диске для публикации
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
    assert type(number_of_pieces('10штбвннерю.tif')) == int, "Возвращает число "
    assert number_of_pieces('2штбвннерю.tif') == 2, "Возвращает число 2"
    assert number_of_pieces('тбвннерю.tif') == 1, "Если явно не указано количество *в штуках Возвращает число 1"

    assert data.propertis_material.get('material', True) == True, 'Материал берется из словаря data.price_material.'


if __name__ == "__main__":
    while True:
        main()
