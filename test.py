# import os
#
# import PIL
# from PIL import Image, ImageDraw, ImageOps
#
#
# def list_file(path_dir: str) -> list[str]:
#     os.chdir(path_dir)  # переходим в указанный катлог
#     print(os.listdir())
#     return os.listdir()  # читаем имена файлов в список
#
#
# def add_border(list_file):
#     for i in list_files:
#         print(i)
#         '''Добавляем контур к файлу для понимания границ печати'''
#         Image.MAX_IMAGE_PIXELS = None
#         with Image.open(i) as img:
#             print(f'открыли {i}')
#             img_border = ImageOps.expand(img, border=100, fill='yellow')  # 1 px color -gray
#
#             img_border.save(i)
#
#
# if __name__ == '__main__':
#     path_dir = input('Введите путь до файлов: ')
#     list_files = list_file(path_dir)
#     add_border(list_files)
