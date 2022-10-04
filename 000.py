from datetime import date
# import PIL
from PIL import Image
import os, zipfile
import data
from tqdm import tqdm


def list_file(path_dir):
    os.chdir(path_dir)  # переходим в указанный катлог
    return os.listdir()  # читаем имена файлов в список


def only_tif(lst: list):  # List whith Only TIF Files
    lst_tif = []
    for i in lst:
        if i.endswith('.tif'):
            lst_tif.append(i)
    return lst_tif


def check_tiff(file_name, material):
    try:
        with Image.open(file_name) as img:
            dpi = data.resolution.get(material)
            s = img.size
            width = round(2.54 * s[0] / dpi, 1)
            length = round(2.54 * s[1] / dpi, 1)
    except PIL.UnidentifiedImageError:
        return print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
Решение: Photoshop / слои / выполнить сведение''')
    # f'Ширина: {width} см\nДлина: {length} см\nРазрешение печати: {dpi} dpi'
    return width, length, dpi


def color_mode(file_name):
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


def size_file(name_file):
    # Размер в МБ
    file_stat = os.stat(name_file)
    # return f'Размер файла: {round(file_stat.st_size / (1024 * 1024), 2)} Mb\n'
    return round(file_stat.st_size / (1024 * 1024), 2)


def write_file_txt(name: str, list_text: str):
    with open(f' {name}_{date.today()}.txt', "w") as file:
        # file.write(list_text)
        print(list_text, file=file)


def calculation(width, length, material):
    price_material = data.price_material.get(material)
    return round(width * length * price_material, 2)


def arh(list_files: list):  # add tif to ZIP file
    for name in tqdm(list_files):
        new_arh = zipfile.ZipFile(f'{date.today()}.zip',"a")
        new_arh.write(name, compress_type=zipfile.ZIP_DEFLATED)
        new_arh.close()


if __name__ == "__main__":
    lst_files = list_file('C:/Users/sasha/Downloads/film (2)')
    lst_tif = only_tif(lst_files)
    lst_all = []
    itog = 0
    with open(f' files_for_print_{date.today()}.txt', "w") as file:

        for i in range(len(lst_tif)):
            w_l_dpi = check_tiff(lst_tif[i], 'banner_440')
            # lst_all.append([lst_tif[i], check_tiff(lst_tif[i], 'banner'), color_mode(lst_tif[i]),
            #                 size_file(lst_tif[i]), calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, 'banner')])
            # print(lst_all)
            print(f'File # {i + 1}: {lst_tif[i]}')
            write_file_txt('TEST', f'File # {i + 1}: {lst_tif[i]}\n')

            print(f'Ширина: {w_l_dpi[0]}см\nДлина {w_l_dpi[1]} см\nРазрешение: {w_l_dpi[2]}dpi')
            print(f'Цветовая модель: {color_mode(lst_tif[i])}')
            print(f'Размер: {size_file(lst_tif[i])} Мб')
            print("-" * 40)

            print(f'Стоимость:{calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, "banner_440")} руб. ')
            itog = itog + calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, "banner_440")
            file.write(f'File # {i + 1}: {lst_tif[i]}\n')
            file.write(f'Ширина: {w_l_dpi[0]} см\nДлина {w_l_dpi[1]} см\nРазрешение: {w_l_dpi[2]} dpi\n')
            file.write(f'Цветовая модель: {color_mode(lst_tif[i])}\n')
            file.write(f'Размер: {size_file(lst_tif[i])} Мб\n')
            file.write("-" * 40 + "\n")
            file.write(f'Стоимость:{calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, "banner_440")} руб. \n\n')
        file.write(f'Итого: {round(itog, 2)} руб.')
    print(f'Итого: {round(itog, 2)} руб.')
    # ar = input('Архивируем: да, нет?: ')
    # if ar == "да":
    arh(lst_tif)
    # else:
    #     print("Exit")
