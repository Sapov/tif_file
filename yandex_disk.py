import os
import shutil
import subprocess
from pathlib import Path

local_path_yadisk = '/home/sasha/Yandex.Disk/upload/'  # фолдер хранения файлов на я.Диске


# local_path_yadisk = 'C:\\Users\\sasha\\YandexDisk\\upload\\' # фолдер хранения файлов на я.Диске

class Yadisk:

    def __init__(self, path):
        self.path = path

    def create_folder(self):
        '''Добавляем фолдер дата
        Директория должна быть всегда уникальной к примеру точная дата мин/сек
        '''
        if os.path.exists(f"{local_path_yadisk}{self.path}"):
            print('Директория уже создана')
        else:
            os.mkdir(f'{local_path_yadisk}{self.path}')

    def add_yadisk_locate(self):
        """закидываем файлы на yadisk локально на ubuntu"""
        Path.cwd()  # Идем в текущий каталог
        lst_files = os.listdir()  # read name files from folder
        for i in lst_files:
            if i.endswith("txt") or i.endswith("zip"):
                print(f'Копирую {i} в {local_path_yadisk}{self.path}')
                shutil.move(i, f'{local_path_yadisk}{self.path}')

    def add_link_from_folder_yadisk(self):
        print(f'Публикую папку: {local_path_yadisk}{self.path}')
        ya_link = subprocess.check_output(["yandex-disk", "publish", f'{local_path_yadisk}{self.path}'])
        ya_link = str(ya_link)
        ya_link = ya_link.lstrip("b'")
        ya_link = ya_link.rstrip(r"\n'")
        print(f'Ссылка на яндекс диск {ya_link}')

        return ya_link
