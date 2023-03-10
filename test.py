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


def number_of_pieces(file_name_in_list: str) -> int:
    '''
    ищем количество в имени файла указываеться после шт
    '''
    file_name_in_list = file_name_in_list.lower()
    if 'шт' in file_name_in_list:
        quantity_in_name_file = file_name_in_list[:file_name_in_list.find('шт')]
        num = ""
        print(file_name_in_list.find('шт'))
        for i in range(file_name_in_list.find('шт') - 1, -1, -1):
            print(file_name_in_list[i])
            if file_name_in_list[i].isdigit():
                num += str(file_name_in_list[i])

            else:
                continue
        num = num[::-1]
        print(int(num))
        return int(num)
    else:
        return 1

number_of_pieces('_440 гратмм12_шт')