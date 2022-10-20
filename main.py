from datetime import date
import PIL
from PIL import Image
import os, zipfile
import data
from tqdm import tqdm
import yandex_disk
import pyinputplus as pyip


def list_file(path_dir: str) -> list[str]:
    os.chdir(path_dir)  # переходим в указанный катлог
    return os.listdir()  # читаем имена файлов в список


def only_tif(lst: list) -> list[str]:  # List whith Only TIF Files
    return [i for i in lst if i.endswith('.tif')]


def check_tiff(file_name: str):
    try:
        Image.MAX_IMAGE_PIXELS = 1000000000
        with Image.open(file_name) as img:
            s = img.size
            resolution = round(img.info['dpi'][0], 0)
            width = round(2.54 * s[0] / resolution, 0)
            length = round(2.54 * s[1] / resolution, 0)

    except PIL.UnidentifiedImageError:
        return print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
Решение: Photoshop / слои / выполнить сведение''')
    return width, length, resolution


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
    with open(f' {name}_{date.today()}.txt', "w") as file:
        print(list_text, file=file)


def calculation(width, length, material: str) -> float:
    price_material = data.price_material.get(material)
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


def select_material() -> str:
    '''Функция выбора материала для печати'''
    # material = pyip.inputMenu([i for i in data.price_material], numbered=True)
    return pyip.inputMenu([i for i in data.price_material], prompt="Выбираем материал для печати: \n", numbered=True)


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


if __name__ == "__main__":
    path_dir = str(input("Введите путь к каталогу: "))

    lst_files = list_file(path_dir)
    material = select_material()
    lst_tif = only_tif(lst_files)

    lst_all = []
    itog = 0
    text_file_name = f'{material}_for_print_{date.today()}.txt'
    with open(text_file_name, "w") as file:

        for i in range(len(lst_tif)):
            w_l_dpi = check_tiff(lst_tif[i])
            assert type(check_tiff(lst_tif[i])) == tuple, 'Ожидаем кортеж'
            file_name = f'File # {i + 1}: {lst_tif[i]}'
            quantity = int(number_of_pieces(lst_tif[i]))
            quantity_print = f'Количество: {quantity} шт.'
            length_width = f'Ширина: {w_l_dpi[0]}см\nДлина {w_l_dpi[1]} см\nРазрешение: {w_l_dpi[2]} dpi'
            color_model = f'Цветовая модель: {color_mode(lst_tif[i])}'
            size = f'Размер: {size_file(lst_tif[i])} Мб'
            price_one = calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, material)
            price = price_one * quantity
            price_print = f'Стоимость:{price_one * quantity} руб.\n '
            itog = itog + price
            file.write(f'{file_name}\n{quantity_print}\n{length_width}\n{color_model}\n{size}\n{price_print}\n')
            file.write("-" * 40 + "\n")
        file.write(f'Итого: {round(itog, 2)} руб.')
    print(f'Итого: {round(itog, 2)} руб.')

    arh(lst_tif, material)  # aрхивация

    path_save = f'upload/Стиль Н/{date.today()}'
    zip_name = f'{material}_{date.today()}.zip'
    print(f'{path_dir}\{zip_name}')
    print(f'{path_save}/{zip_name}')

    yandex_disk.create_folder(path_save)
    yandex_disk.upload_file(rf'{path_dir}\{zip_name}', f'{path_save}/{zip_name}')
    yandex_disk.upload_file(rf'{path_dir}\{text_file_name}', f'{path_save}/{text_file_name}')

    assert type(number_of_pieces('10штбвннерю.tif')) == int, "Возвращает число "
    assert number_of_pieces('2штбвннерю.tif') == 2, "Возвращает число 2"
    assert number_of_pieces('тбвннерю.tif') == 1, "Если явно не указано количество *в штуках Возвращает число 1"

    assert data.price_material.get('material', True) == True, 'Материал берется из словаря data.price_material.'
    assert type(path_dir) == str, 'Должна быть строка'
    assert type(list_file(path_dir)) == list
    assert type(only_tif(lst_files)) == list, "Список list_file  должен быть list (списком)"
    assert type(lst_files) == list, "Список list_file  должен быть list (списком)"





