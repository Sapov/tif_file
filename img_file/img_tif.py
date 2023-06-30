import PIL
from PIL import Image, ImageOps
import data


def perimetr(width, length):
    ''' Вычисляем прериметр изображения'''
    return (width + length) * 2


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
        if self.type_print == 'Широкоформатная печать':
            for i in self.lst_tif:
                if self.check_tiff(i)[2] > data.propertis_material_sirka.get(self.material)[1]:
                    print("[INFO] Разрешение больше необходимого Уменьшаем!!")
                    self.resize_image(i, data.propertis_material_sirka.get(self.material)[1])
                elif self.check_tiff(i)[2] == data.propertis_material_sirka.get(self.material)[1]:
                    print('[INFO] Разрешение соответствует требованиям')
                else:
                    print("[INFO] Низкое разрешение не соответствует требованиям")

        elif self.type_print == 'Интерьерная печать':
            for i in self.lst_tif:
                if self.check_tiff(i)[2] > data.propertis_material_interierka.get(self.material)[1]:
                    print("[INFO] Разрешение больше необходимого Уменьшаем!!")
                    self.resize_image(i, data.propertis_material_interierka.get(self.material)[1])
                elif self.check_tiff(i)[2] == data.propertis_material_interierka.get(self.material)[1]:
                    print('[INFO] Разрешение соответствует требованиям')
                else:
                    print("[INFO] Низкое разрешение не соответствует требованиям")


        elif self.type_print == 'УФ-Печать':
            for i in self.lst_tif:
                if self.check_tiff(i)[2] > data.propertis_material_UV.get(self.material)[1]:
                    print("[INFO] Разрешение больше необходимого Уменьшаем!!")
                    self.resize_image(i, data.propertis_material_UV.get(self.material)[1])
                elif self.check_tiff(i)[2] == data.propertis_material_UV.get(self.material)[1]:
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
