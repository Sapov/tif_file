from PIL import Image
import os


def check_tiff(file_name, material):
    '''
    :param file_name: Принимаем имя файла
    :param material:  принимаем параметре материала banner  -> 72 dpi или interier ->150 dpi
    :return:
    # проверка что файлы для печати баннеров пеатаются с разрешением 72 DPI
    # а файлы с для печати пленки или инреьерной печати разрешением 150 DPI
    '''

    if material == 'banner':
        dpi = 72
    elif material == 'interier':
        dpi = 150

    with Image.open(file_name) as img:
        s = img.size
        width = round(2.54 * s[0] / dpi, 1)
        length = round(2.54 * s[1] / dpi, 1)
        # print("Ширина: ", width, 'см.\n', 'Длина :', length, 'см.')
        color_mode = img.mode
        if color_mode == 'CMYK':
            print('[x]........Color Mode Valid: ', color_mode, '\n')
        else:
            print("Цветовая модель не соответствует требованиям, нужно перевести в CMYK")

    return (width, length, color_mode, dpi)
