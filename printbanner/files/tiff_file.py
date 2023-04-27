import os

import PIL
from PIL import Image, ImageOps



def thumbnail(file_name: str):
    '''создание `thumbnail`'''
    # for i in lst_tif:
    Image.MAX_IMAGE_PIXELS = None
    with Image.open(file_name) as img:
        size = (150, 150)
        img.thumbnail(size)
        path_preview = f'media/preview/thumbnail_{str(file_name)[:-4]}.jpg'
        img.save(path_preview)
        return path_preview[5:]


def check_tiff(file_name: str):
    '''
    :param file_name: принимает имя файла
    :return: возвращает кортеж (длина ширина (см) и разрешение файла (dpi)
    '''

    try:
        Image.MAX_IMAGE_PIXELS = None
        with Image.open(file_name) as img:
            width, length = img.size
            resolution = round(img.info['dpi'][0], 0)
            width = round(2.54 * width / resolution, 0)
            length = round(2.54 * length / resolution, 0)

    except PIL.UnidentifiedImageError:

        return print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
Решение: Photoshop / слои / выполнить сведение''')

    return width, length, resolution
