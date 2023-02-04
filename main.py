from datetime import date, datetime
import PIL
from PIL import Image
import os
import zipfile
import data
from tqdm import tqdm

import img_file.img_tif
import yandex_disk
from pyinputplus import inputMenu
import send_mail
from img_file.img_tif import check_resolution


def list_file(path_dir: str) -> list[str]:
    os.chdir(path_dir)  # переходим в указанный катлог
    return os.listdir()  # читаем имена файлов в список


def only_tif(lst: list) -> list[str]:  # List whith Only TIF Files
    return [i for i in lst if i.endswith('.tif')]


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


# def calculation(width, length, material: str) -> float:
#     price_material = data.price_material.get(material)
#     return round(width * length * price_material, 2)

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


# def select_material() -> str:
#     '''Функция выбора материала для печати'''
#     # material = pyip.inputMenu([i for i in data.price_material], numbered=True)
#     return inputMenu([i for i in data.price_material], prompt="Выбираем материал для печати: \n", numbered=True)
def select_material() -> str:
    '''Функция выбора материала для печати'''
    return inputMenu([i for i in data.propertis_material], prompt="Выбираем материал для печати: \n", numbered=True)


def select_oraganization():
    '''
    Выбор организации для отправки файлов
         '''
    return inputMenu([i for i in data.organisations], prompt='Выбирите организацию куда отправить файлы: \n',
                     numbered=True)


def number_of_pieces(file_name_in_list: str) -> int:
    '''
    ищем количество в имени файла указываеться после шт
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
def rec_to_file(text_file_name: str):
    itog = 0
    with open(text_file_name, "w") as file:
        for i in range(len(lst_tif)):
            w_l_dpi = img_file.img_tif.check_tiff(lst_tif[i])
            assert type(img_file.img_tif.check_tiff(lst_tif[i])) == tuple, 'Ожидаем кортеж'
            file_name = f'File # {i + 1}: {lst_tif[i]}'
            quantity = int(number_of_pieces(lst_tif[i]))
            quantity_print = f'Количество: {quantity} шт.'
            length_width = f'Ширина: {w_l_dpi[0]} см\nДлина: {w_l_dpi[1]} см\nРазрешение: {w_l_dpi[2]} dpi'
            color_model = f'Цветовая модель: {color_mode(lst_tif[i])}'
            size = f'Размер: {size_file(lst_tif[i])} Мб'
            price_one = calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, material)
            square_unit = (w_l_dpi[0] * w_l_dpi[
                1]) / 10000  # площадь печати одной штуки (см приводим к метрам  / 10 000
            square = f'Площадь печати {round(square_unit * quantity,2)} м2'  # вся площадь печати
            price = price_one * quantity
            price_print = f'Стоимость: {price_one * quantity} руб.\n '
            itog = itog + price
            file.write(f'{file_name}\n{quantity_print}\n{length_width}\n{square}\n{color_model}\n{size}\n{price_print}\n')
            file.write("-" * 40 + "\n")

        file.write(f'Итого: {round(itog, 2)} руб.\n')
        print(f'Итого стоимость печати: {round(itog, 2)} руб.')


def file_sale(file_s: str):
    itog = 0
    with open(file_s, "w") as file:
        for i in range(len(lst_tif)):
            w_l_dpi = img_file.img_tif.check_tiff(lst_tif[i])
            assert type(img_file.img_tif.check_tiff(lst_tif[i])) == tuple, 'Ожидаем кортеж'
            file_name = f'File # {i + 1}: {lst_tif[i]}'
            quantity = int(number_of_pieces(lst_tif[i]))
            quantity_print = f'Количество: {quantity} шт.'
            length_width = f'Ширина: {w_l_dpi[0]} см\nДлина: {w_l_dpi[1]} см\nРазрешение: {w_l_dpi[2]} dpi'
            square_unit = (w_l_dpi[0] * w_l_dpi[1]) / 10000 # площадь печати одной штуки (см приводим к метрам  / 10 000
            square = f'Площадь печати {round(square_unit * quantity,2)} м2' # вся площадь печати
            color_model = f'Цветовая модель: {color_mode(lst_tif[i])}'
            size = f'Размер: {size_file(lst_tif[i])} Мб'
            price_one = calculation_for_client(w_l_dpi[0] / 100, w_l_dpi[1] / 100, material)  # считаем стоимость для заказчика
            price = price_one * quantity
            price_print = f'Стоимость: {price_one * quantity} руб.\n '
            itog = itog + price
            file.write(f'{file_name}\n{quantity_print}\n{length_width}\n{square}\n{color_model}\n{size}\n{price_print}\n')
            file.write("-" * 40 + "\n")

        file.write(f'Итого: {round(itog, 2)} руб.\n')
        print(f'Итого продажа: {round(itog, 2)} руб.')


if __name__ == "__main__":
    path_dir = str(input("Введите путь к каталогу: "))
    client = input('Введите им клиента: ')
    # path_dir = 'C:/Users/Sasha/Downloads/замена баннеры311022'
    lst_files = list_file(path_dir)
    material = select_material()
    lst_tif = only_tif(lst_files)

    check_resolution(lst_tif, material)  # Меняем разрешение на стандарт

    text_file_name = f'{material}_for_print_{date.today()}.txt'
    rec_to_file(text_file_name)
    file_s = f'{client}_{material}_for_sale_{date.today()}.txt'
    file_sale(file_s)

    arh(lst_tif, material)  # aрхивация
    organizations = select_oraganization()
    path_save = f'upload/{organizations}/{date.today()}'
    zip_name = f'{material}_{date.today()}.zip'
    print(f'{path_dir}\{zip_name}')
    print(f'{path_save}/{zip_name}')

    # def upload_all_in_yadisk():
    # yandex_disk.create_folder(path_save)
    # yandex_disk.upload_file(rf'{path_dir}\{zip_name}', f'{path_save}/{zip_name}')
    # link = yandex_disk.get_download_link(path_save)
    # yandex_disk.upload_file(rf'{path_dir}\{text_file_name}',
    #                         f'{path_save}/{text_file_name}')  # send text file from disk

    with open(text_file_name) as file:
        new_str = file.read()
        send_mail.send_mail(message=f'{new_str} \nCсылка на архив: {link}', subject=material)

    assert type(number_of_pieces('10штбвннерю.tif')) == int, "Возвращает число "
    assert number_of_pieces('2штбвннерю.tif') == 2, "Возвращает число 2"
    assert number_of_pieces('тбвннерю.tif') == 1, "Если явно не указано количество *в штуках Возвращает число 1"

    assert data.propertis_material.get('material', True) == True, 'Материал берется из словаря data.price_material.'
    assert type(path_dir) == str, 'Должна быть строка'
    assert type(list_file(path_dir)) == list
    assert type(only_tif(lst_files)) == list, "Список list_file  должен быть list (списком)"
    assert type(lst_files) == list, "Список list_file  должен быть list (списком)"
