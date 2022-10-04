from datetime import date
import PIL
from PIL import Image
import os
import data


def list_file(path_dir):
    '''
    получаем список файлов данного каталога
        :param path_dir: путь до каталога
        :return: возвращаем список list_files
        '''
    os.chdir(path_dir)  # переходим в указанный катлог
    return os.listdir()  # читаем имена файлов в список


def calculation(width, length, material):
    '''
    расчет стоимости печати
    :param width: Ширина
    :param length: длина
    :param material: материал
    :return: стоимость
    '''
    price_material = data.price_material.get(material)
    return width * length * price_material


def check_tiff(file_name, material):
    '''
    :param file_name: Принимаем имя файла
    :param material:  принимаем параметре материала banner  -> 72 dpi или interier ->150 dpi
    :return:
    # проверка что файлы для печати баннеров пеатаются с разрешением 72 DPI
    # а файлы с для печати пленки или инреьерной печати разрешением 150 DPI
    '''

    try:
        with Image.open(file_name) as img:
            dpi = data.resolution.get(material)
            s = img.size
            width = round(2.54 * s[0] / dpi, 1)
            length = round(2.54 * s[1] / dpi, 1)
    except PIL.UnidentifiedImageError:
        return print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
Решение: Photoshop / слои / выполнить сведение''')

    return width, length, dpi

def color_mode(material):
    try:
        with Image.open(file_name) as img:
            color_mode = img.mode
            if color_mode == 'CMYK':
                print('[x]........Color Mode Valid: ', color_mode, '\n')
                return color_mode
            else:
                print("Цветовая модель не соответствует требованиям, нужно перевести в CMYK")
                return color_mode
    except PIL.UnidentifiedImageError:
        print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
            Решение: Photoshop / слои / выполнить сведение''')
        return color_mode


def create_file_list(out_path, material):
    '''
    Функиця записывает в файл:
     1) имена файлов
     2) размер печати файлов
     3) размер файла в мб
     3) стоимость печати каждого фйала
    :param out_path:
    :return:
    '''
    lst_f = list_file(out_path)
    itog = 0
    with open(f' files_for_print_{date.today()}.txt', "w") as file_in_list:


        zaglavie_fila = f' {"-" * 14} Список файлов для печати на: {date.today()}{"-" * 10}\n\n'
        file_in_list.write(zaglavie_fila)
        print(zaglavie_fila)
        # Пишем в файл имена файлов
        for name_file in range(len(lst_f)):
            if lst_f[name_file].endswith('.tif'):
                # file_name = f'File #{name_file + 1}: {lst_f[name_file]}\n'
                # file_in_list.write(file_name)

                # Ширина длина
                img_properis = check_tiff(lst_f[name_file], material)
                img_propertis_file = f'Ширина: {img_properis[0]} см\nДлина: {img_properis[1]} см\nРазрешение печати: {img_properis[2]} dpi\n'
                print(img_propertis_file)
                file_in_list.write(img_propertis_file)

                # Размер в МБ
                file_stat = os.stat(lst_f[name_file])
                size_file = f'Размер файла: {round(file_stat.st_size / (1024 * 1024), 2)} Mb\n'
                print(size_file)
                file_in_list.write(size_file)

                # # Стоимость печати

                price = round(calculation(img_properis[0] / 100, img_properis[1] / 100, material), 2)
                file_in_list.write("-" * 25 + " \n")
                file_in_list.write(f'Стоимость {price} руб.\n\n')
                print(price, 'РУБ.')
                itog = itog + price
        print('ИТОГО:', round(itog, 2))
        file_in_list.write(f'ИТОГО: {round(itog, 2)} руб.\n\n')
def file_write(lsit, name_file):

if __name__ == '__main__':
    out_path = input("Введите путь к каталогу: ")
    material = input("Материал Баннер (banner) или Пленка (film)?: ")
    # create_file_list('C:/Users/User/Downloads/баннер220922', 'banner')
    create_file_list(out_path, material)
