import os
from datetime import date
'''Создаем файл - задание для печати--
Выводим список имен файлов в текстовый файл '''

ouit_path = input("Введите путь к каталогу: ")
os.chdir(ouit_path)  # переходим в указанный катлог
lst_f = os.listdir()  # читаем имена файлов в список
list_file = open(f' files_for_print_{date.today()}.txt', "w")  # открываем файл на чтение и пишем имена файлов
print('-' * 20, "Список файлов для печати на", date.today(), '-' * 20)
list_file.write(f' {"-" * 10} Список файлов для печати на: {date.today()}{"-" * 10}\n')
for i in range(len(lst_f)):
    print(f'File #{i + 1}: {lst_f[i]}')
    list_file.write(f'File #{i + 1}: {lst_f[i]}\n')
list_file.close()