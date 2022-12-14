import PIL
from PIL import Image
import data

def resize_image(file_name: str, new_dpi: int):
    '''
    :param file_name: имя фала для ресайза
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
        print(f'Изменил размер файла {file_name} c {resolution} dpi на {new_dpi} dpi\n')

    except PIL.UnidentifiedImageError:
        return print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
Решение: Photoshop / слои / выполнить сведение''')


def check_tiff(file_name: str):
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



def check_resolution(lst_tif, material):
    '''
    Проверяем разрешения и уменьшаем в соответстввии со стандартом
    :param lst_tif:
    :param material:
    :return:
    '''
    for i in lst_tif:
        if check_tiff(i)[2] > data.propertis_material.get(material)[1]:
            print("Разрешение больше Уменьшаем")
            resize_image(i, data.propertis_material.get(material)[1])
        else:
            print("Меньше Увеличиваем?? или оставляем")
        # print(i)
