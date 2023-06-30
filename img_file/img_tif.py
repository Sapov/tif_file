import os
from datetime import date

import PIL
from PIL import Image, ImageOps
import data


def add_border(lst_tif: list):
    '''Добавляем контур к файлу для понимания границ печати'''
    for i in lst_tif:
        Image.MAX_IMAGE_PIXELS = None
        with Image.open(i) as img:
            img_border = ImageOps.expand(img, border=100, fill='red')  # 1 px color -gray
            #
            img_border.save(f'border_{i}')
            print(f' Сделали обводку у файла: {i}')


def thumbnail(lst_tif: list):
    '''создание `thumbnail`'''
    for i in lst_tif:
        Image.MAX_IMAGE_PIXELS = None
        with Image.open(i) as img:
            size = (150, 150)
            img.thumbnail(size)
            img.save(f'thumbnail_{i[:-4]}.jpg')


class CheckImage:
    '''Работа с файлом TIFF'''

    def __init__(self, type_print, lst_tif, material):
        self.file_name = None  # имя файла
        self.type_print = type_print  # тип печати
        self.lst_tif = lst_tif  # Список тиф файлов
        self.material = material
        self.width = None  # Ширина файла
        self.length = None  # Длина файла
        self.resolution = None  # Разрешение файла

    def resize_image(file_name: str, new_dpi: int):
        '''
        :param file_name: имя файла для ресайза
        :param new_dpi: новое разрешение ресайза
        :return:
        '''
        if new_dpi <= 0:
            return print("Нельзя устанавливать отрицательное разрешение или  0")
        try:
            Image.MAX_IMAGE_PIXELS = None
            with Image.open(file_name) as img:
                width_px, length_px = img.size
                resolution = round(img.info['dpi'][0], 0)
                persent_resize = float(new_dpi / resolution)
                width_new_px = round(float(persent_resize * width_px), 0)
                length_new_px = round((width_new_px / width_px) * length_px, 0)
                img = img.resize((int(width_new_px), int(length_new_px)))
                # img.save(f'new{file_name}', dpi=(new_dpi, new_dpi))
                img.save(f'{file_name}', dpi=(new_dpi, new_dpi))
            print(f'[INFO] Изменил размер файла {file_name} c {resolution} dpi на {new_dpi} dpi\n')

        except PIL.UnidentifiedImageError:
            return print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
                Решение: Photoshop / слои / выполнить сведение''')

    def check_resolution(self):
        '''
        Проверяем разрешения и уменьшаем в соответствии со стандартом
        :param lst_tif:
        :param material:
        :return:
        '''
        for i in self.lst_tif:
            if self.check_tiff(i)[2] > data.type_print[self.type_print][1]:
                print("[INFO] Разрешение больше необходимого Уменьшаем!!")
                self.resize_image(i, data.type_print[self.type_print][1])
            elif self.check_tiff(i)[2] == data.type_print[self.type_print][1]:
                print('[INFO] Разрешение соответствует требованиям')
            else:
                print("[INFO] Низкое разрешение не соответствует требованиям")

    def check_tiff(self, file_name: str):
        '''
        :param file_name: принимает имя файла
        :return: возращает кортеж (длина, ширина (см) и разрешение файла (dpi)
        '''

        try:
            Image.MAX_IMAGE_PIXELS = None
            with Image.open(file_name) as img:
                width, length = img.size
                self.resolution = round(img.info['dpi'][0], 0)
                self.width = round(2.54 * width / self.resolution, 0)
                self.length = round(2.54 * length / self.resolution, 0)

        except PIL.UnidentifiedImageError:

            return print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
    Решение: Photoshop / слои / выполнить сведение''')

        return self.width, self.length, self.resolution

    def perimetr(self):
        ''' Вычисляем прериметр изображения'''
        return (self.width + self.length) * 2

    def color_mode(self, file_name) -> str:
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

    def number_of_pieces(self, file_name_in_list) -> int:
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

    def size_file(self, file_name) -> float:
        # Размер в МБ
        file_stat = os.stat(file_name)
        return round(file_stat.st_size / (1024 * 1024), 2)

    def calculation(self, width, length, material: str) -> float:
        price_material = data.type_print[self.type_print][0]
        print(price_material)
        return round(width * length * price_material, 2)

    # запись в текстовый файл
    def rec_to_file(self, ):
        text_file_name = f'{self.material}_for_print_{date.today()}.txt'
        itog = 0

        with open(text_file_name, "w") as file:
            for i in range(len(self.lst_tif)):
                w_l_dpi = self.check_tiff(self.lst_tif[i])
                assert type(self.check_tiff(self.lst_tif[i])) == tuple, 'Ожидаем кортеж'
                # P = self.perimetr(w_l_dpi[0], w_l_dpi[1])  # периметр файла
                P = self.perimetr()  # периметр файла

                file_name = f'File # {i + 1}: {self.lst_tif[i]}'
                quantity = int(self.number_of_pieces(self.lst_tif[i]))
                quantity_print = f'Количество: {quantity} шт.'
                length_width = f'Ширина: {w_l_dpi[0]} см\nДлина: {w_l_dpi[1]} см\nРазрешение: {w_l_dpi[2]} dpi'
                color_model = f'Цветовая модель: {self.color_mode(self.lst_tif[i])}'
                size = f'Размер: {self.size_file(self.lst_tif[i])} Мб'
                price_one = self.calculation(w_l_dpi[0] / 100, w_l_dpi[1] / 100, self.material)
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
