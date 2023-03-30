import os

import PIL
from PIL import Image


class Banner:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return (self.width + self.length) * 2

    def square(self):
        ''' вычисление площади баннера
        * / 10000 # площадь печати одной штуки (см приводим к метрам / 10 000 '''
        return (self.width * self.length) / 10000

    def count_luvers(self, distance):
        ''' подсчитываем количество люверсов на 1 метре
        distance - расстояние между люверсами'''
        return int((self.width + self.length) * 2 * 100 / distance)

    def only_tif(lst: list) -> list[str]:  # List whith Only TIF Files
        ''' выбираем только TIF файлы'''
        return [i for i in lst if i.endswith('.tif') or i.endswith('.tiff')]

    # Люверсы под загиб


# banner = Banner(2, 4)
# print(banner.perimeter())
# print(banner.square())
# print(banner.count_luvers(30))
#
# print(Banner(2, 3).perimeter())
# print(Banner(2, 3).square())
# # print(Banner(2, 3).count_luvers(30))
#
#
# # Люверсы под загиб баннер 2х3 м
# print(Banner(2, 3).count_luvers(30))

class WorkFile:

    def __init__(self, name_file):
        self.name_file = name_file

    def check_type_file(self):
        if self.name_file.endswith('.tif') or self.name_file.endswith('.tiff'):
            print('TIFF')
            return "YES"
        elif self.name_file.endswith('.cdr'):
            print('CDR')
            return 'NO'

    def color_mode(self) -> str:
        Image.MAX_IMAGE_PIXELS = None
        try:
            with Image.open(self.name_file) as img:
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

    def size_file(self) -> float:
        # Размер в МБ
        file_stat = os.stat(self.name_file)
        return round(file_stat.st_size / (1024 * 1024), 2)




# print(WorkFile('test.cdr').check_type_file())
# print(WorkFile('printbanner/media/image/15_03_23/8шт_баннер_420х594мм_безполяАTEST_AHsq3ke.tif').color_mode())
# print(WorkFile('printbanner/media/image/15_03_23/8шт_баннер_420х594мм_безполяАTEST_AHsq3ke.tif').size_file())
