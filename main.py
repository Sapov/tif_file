from datetime import date
import PIL
from PIL import Image
import os, zipfile
import data
from tqdm import tqdm
import yandex_disk
import time


def list_file(path_dir: str) -> list[str]:
    os.chdir(path_dir)  # переходим в указанный катлог
    return os.listdir()  # читаем имена файлов в список


def only_tif(lst: list) -> list[str]:  # List whith Only TIF Files
    return [i for i in lst if i.endswith('.tif')]


def check_tiff(file_name: str):
    try:
        with Image.open(file_name) as img:
            s = img.size
            resolution = round(img.info['dpi'][0],0)
            width = round(2.54 * s[0] / resolution,0)
            length = round(2.54 * s[1] / resolution,0)

    except PIL.UnidentifiedImageError:
        return print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
Решение: Photoshop / слои / выполнить сведение''')
    return width, length, resolution


def color_mode(file_name: str) -> str:
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


def calculation(width, length, material: str):
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


if __name__ == "__main__":
    path_dir = input("Введите путь к каталогу: ")
    lst_files = list_file(path_dir)
    material = input("Материал Баннер (banner_440) или Пленка (film)?: ")
    lst_tif = only_tif(lst_files)
    lst_all = []
    itog = 0
    with open(f' {material}_for_print_{date.today()}.txt', "w") as file:

        for i in range(len(lst_tif)):
            w_l_dpi = check_tiff(lst_tif[i])
            # lst_all.append([lst_tif[i], check_tiff(lst_tif[i], 'banner'), color_mode(lst_tif[i]),
            #                 size_file(lst_tif[i]), calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, 'banner')])
            # print(lst_all)
            print(f'File # {i + 1}: {lst_tif[i]}')

            print(f'Ширина: {w_l_dpi[0]}см\nДлина {w_l_dpi[1]} см\nРазрешение: {w_l_dpi[2]} dpi')
            print(f'Цветовая модель: {color_mode(lst_tif[i])}')
            print(f'Размер: {size_file(lst_tif[i])} Мб')
            print("-" * 40)

            print(f'Стоимость:{calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, material)} руб. ')
            itog = itog + calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, material)
            file.write(f'File # {i + 1}: {lst_tif[i]}\n')
            file.write(f'Ширина: {w_l_dpi[0]} см\nДлина {w_l_dpi[1]} см\nРазрешение: {w_l_dpi[2]} dpi\n')
            file.write(f'Цветовая модель: {color_mode(lst_tif[i])}\n')
            file.write(f'Размер: {size_file(lst_tif[i])} Мб\n')
            file.write("-" * 40 + "\n")
            file.write(f'Стоимость:{calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, material)} руб. \n\n')
        file.write(f'Итого: {round(itog, 2)} руб.')
    print(f'Итого: {round(itog, 2)} руб.')

    arh(lst_tif, material)

    path_save = f'upload/Стиль Н/{date.today()}'
    zip_name = f'{material}_{date.today()}.zip'
    print(f'{path_dir}\{zip_name}')
    print(f'{path_save}/{zip_name}')

    yandex_disk.create_folder(path_save)
    yandex_disk.upload_file(rf'{path_dir}\{zip_name}', f'{path_save}/{zip_name}')

# upload_file(r"C:\temp\1.7z", 'TEST2/1.7z')
