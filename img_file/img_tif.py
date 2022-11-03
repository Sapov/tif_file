# import PIL
# from PIL import Image
#
#
# def resize_image(file_name: str, new_dpi: int):
#     '''
#     :param file_name: имя фала для ресайза
#     :param new_dpi: новое разрешение ресайза
#     :return:
#     '''
#     if new_dpi <= 0:
#         return print("Нельзя устанавливать отрицательное разрешение или  0")
#     try:
#         Image.MAX_IMAGE_PIXELS = None
#         with Image.open(file_name) as img:
#             width_px, length_px = img.size
#             resolution = round(img.info['dpi'][0], 0)
#             persent_resize = float(new_dpi / resolution)
#             width_new_px = round(float(persent_resize * width_px), 0)
#             length_new_px = round((width_new_px / width_px) * length_px, 0)
#             img = img.resize((int(width_new_px), int(length_new_px)))
#             img.save(file_name, dpi=(new_dpi, new_dpi))
#         print(f'Изменил размер файла {file_name} c {resolution} dpi на {new_dpi} dpi')
#
#     except PIL.UnidentifiedImageError:
#         return print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
# Решение: Photoshop / слои / выполнить сведение''')
#
#
# def check_image_tiff(file_name: str):
#     try:
#         Image.MAX_IMAGE_PIXELS = None
#         with Image.open(file_name) as img:
#             width, length = img.size
#             resolution = round(img.info['dpi'][0], 0)
#             width = round(2.54 * width / resolution, 0)
#             length = round(2.54 * length / resolution, 0)
#
#     except PIL.UnidentifiedImageError:
#
#         return print('''!!! -- Это ошибка: Не сведенный файл Tif --- !!!
# Решение: Photoshop / слои / выполнить сведение''')
#     print(f'width: {width} cm, length:{length}cm resolution: {resolution}dpi')
#
#     return width, length, resolution
#
#
# # def chack_resolution(width: float, length: float,  resolution: int)
# #     if resolution

from pyinputplus import inputMenu
import data


def calculation(width, length, material: str) -> float:
    price_material = data.propertis_material.get(material)[0]
    print(price_material)
    # return round(width * length * price_material, 2)

# select_material()
calculation(1, 2, "banner_440")
