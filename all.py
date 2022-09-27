# from PIL import Image
#
# image_path = 'C:/Users/User/Downloads/баннер220922/30шт_баннер_503х707мм_безполя.tif'
# dpi = 72
# img = Image.open(image_path)
# s = img.size
# print(s)
# length_x, width_y = s
# factor = min(1, float(1024.0 / length_x))
# print(factor)
# size = int(factor * length_x), int(factor * width_y)
# print(size)
#
# # изменяем размер
# new_image = img.resize(s)
# new_image.show()
# # сохранение картинки
# new_image.save('C:/Users/User/Downloads/баннер220922/2.tif', dpi=(dpi, dpi))
# width = round(2.54 * s[0] / dpi, 1)
# length = round(2.54 * s[1] / dpi, 1)
# print("При dpi=", dpi, "Ширина: ", width, 'см.\n', 'Длина :', length, 'см.')

#
#     image_resize = img.resize(size)
#     # image_resize.save('C:/Users/User/Downloads/баннер220922/test.tiff')
#     # image_resize = img.resize(size, Image.ANTIALIAS)
#     # temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='1.png')
#     # temp_filename = temp_file.name
#     image_resize.save('C:/Users/User/Downloads/баннер220922/test.tiff', dpi=(300, 300))
#     # return temp_filename
#


# def set_image_dpi_resize(image):
#     """
#     Rescaling image to 300dpi while resizing
#     :param image: An image
#     :return: A rescaled image
#     """
#     with Image.open(image) as img:
#         s = img.size
#         print(s)
#
#     length_x, width_y = s
#     factor = min(1, float(1024.0 / length_x))
#     print(factor)
#     size = int(factor * length_x), int(factor * width_y)
#     print(size)
#     image_resize = img.resize(size)
#     # image_resize.save('C:/Users/User/Downloads/баннер220922/test.tiff')
#     # image_resize = img.resize(size, Image.ANTIALIAS)
#     # temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='1.png')
#     # temp_filename = temp_file.name
#     image_resize.save('C:/Users/User/Downloads/баннер220922/test.tiff', dpi=(300, 300))
#     # return temp_filename
#
# set_image_dpi_resize('C:/Users/User/Downloads/баннер220922/30шт_баннер_503х707мм_безполя.tif')
#

def go():
    a = input('Enter:')
    if a == 1:
        return "Ok"
    elif a == 2:
        return "not ok"

print(go())
