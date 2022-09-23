import os
from datetime import date

import tiff
from tiff import check_tiff

def create_file_list(out_path):
    os.chdir(out_path)  # переходим в указанный катлог
    lst_f = os.listdir()  # читаем имена файлов в список
    list_file = open(f' files_for_print_{date.today()}.txt', "w")  # открываем файл на чтение и пишем имена файлов
    zaglavie_fila = f' {"-" * 10} Список файлов для печати на: {date.today()}{"-" * 10}\n\n'
    list_file.write(zaglavie_fila)
    print(zaglavie_fila)
    for file in range(len(lst_f)):
        if lst_f[file].endswith('.tif'):
            file_name = f'File #{file + 1}: {lst_f[file]}\n'
            list_file.write(file_name)
            print(file_name)
            img_properis = tiff.check_tiff(lst_f[file],'banner')
            img_propertis_file = f'Ширина: {img_properis[0]} см\nДлина: {img_properis[1]} см\nЦветовая модель: {img_properis[2]} \nРазрешение печати: {img_properis[3]} dpi\n\n'
            print(img_propertis_file)
            list_file.write(img_propertis_file)

    list_file.close()

# out_path = input("Введите путь к каталогу: ")

create_file_list(out_path='C:/Users/User/Downloads/баннер220922')