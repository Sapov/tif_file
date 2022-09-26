import os
from datetime import date

import tiff

def create_file_list(out_path, material):
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
            img_properis = tiff.check_tiff(lst_f[file], material)
            img_propertis_file = f'Ширина: {img_properis[0]} см\nДлина: {img_properis[1]} см\nЦветовая модель: {img_properis[2]} \nРазрешение печати: {img_properis[3]} dpi\n'
            print(img_propertis_file)
            list_file.write(img_propertis_file)
            file_stat = os.stat(lst_f[file])
            size_file = f'Размер файла: {round(file_stat.st_size / (1024 * 1024), 2)} Mb\n\n'
            # print((os.path.getsize(lst_f[file])/1024*1024,"MB" ))
            print(size_file)
            list_file.write(size_file)
    list_file.close()


out_path = input("Введите путь к каталогу: ")
material = input("Материал Баннер (banner) или Пленка (film)?: ")

create_file_list(out_path, material)
