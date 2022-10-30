import requests
import data
from ya_token import yandex_TOKEN

TOKEN = yandex_TOKEN
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def create_folder(path):
    """Создание папки. \n path: Путь к создаваемой папке."""
    requests.put(f'{URL}?path={path}', headers=headers)
    print(requests.put(f'{URL}?path={path}', headers=headers))


def delete_folder(path: str):
    """deleting папки. \n path: Путь к создаваемой папке."""
    requests.delete(f'{URL}?path={path}', headers=headers)
    print(requests.delete(f'{URL}?path={path}', headers=headers))


# delete_folder(f'upload/Стиль Н/{date.today()}')
def upload_file(loadfile, savefile, replace=False):
    """Загрузка файла.
    savefile: Путь к файлу на Диске
    loadfile: Путь к загружаемому файлу
    replace: true or false Замена файла на Диске"""
    res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    with open(loadfile, 'rb') as f:
        try:
            requests.put(res['href'], files={'file': f})
        except KeyError:
            print(res)


# upload_file(r"C:\temp\1.7z", 'TEST2/1.7z')


def backup(savepath, loadpath):
    """Загрузка папки на Диск. \n savepath: Путь к папке на Диске для сохранения \n loadpath: Путь к загружаемой папке"""
    date_folder = '{0}_{1}'.format(loadpath.split('\\')[-1], datetime.now().strftime("%Y.%m.%d-%H.%M.%S"))
    create_folder(savepath)
    for address, _, files in os.walk(loadpath):
        create_folder('{0}/{1}/{2}'.format(savepath, date_folder, address.replace(loadpath, "")[1:].replace("\\", "/")))
        # bar = Bar('Loading', fill='X', max=len(files))
        for file in files:
            upload_file('{0}\{1}'.format(address, file), \
                        '{0}/{1}{2}/{3}'.format(savepath, date_folder, address.replace(loadpath, "").replace("\\", "/"),
                                                file))


def get_download_link(path: str) -> str:
    """получаем сссылку к папке на скачивание"""
    requests.get(f'{URL}/download?path={path}', headers=headers)
    print(requests.get(f'{URL}/download?path={path}', headers=headers))
    r = requests.get(f'{URL}/download?path={path}&fields=list', headers=headers)
    di = r.json()
    return di['href']

#
# get_download_link('upload/Стиль Н/2022-10-13')
