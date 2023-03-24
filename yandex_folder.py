import requests
import configparser

upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
folder_url = "https://cloud-api.yandex.net/v1/disk/resources"


class Yandex_disk:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("TOKENS_DANGER.ini")
        self.token = config['YANDEX']['ya_token']

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def new_folder(self, folder_name):                                                              # создание новой папки на Диске
        url = folder_url
        headers = self.get_headers()
        response = requests.put(f'{url}?path={folder_name}', headers=headers)
        print(response)
        return 'Папка успешно создана!'

    def delete_folder(self, folder_name):
        url = folder_url
        headers = self.get_headers()
        response = requests.delete(f'{url}?path={folder_name}', headers=headers)
        print(response)
        return 'Старая папка удалена!'


folder = Yandex_disk()
folder_name = 'Учебная тревога'
a = folder.delete_folder(folder_name)
b = folder.new_folder(folder_name)

