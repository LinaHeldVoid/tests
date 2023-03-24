import unittest
import requests
import configparser

from yandex_folder import Yandex_disk, folder_url, folder_name


class Yandex_folder_test(unittest.TestCase):

    def test(self):
        name = folder_name
        url = folder_url
        config = configparser.ConfigParser()
        config.read("TOKENS_DANGER.ini")
        token = config['YANDEX']['ya_token']
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {token}'
        }
        response = requests.get(f'{url}?path={name}', headers=headers)
        dictionary = response.json()
        dict_pattern = {'message': 'Не удалось найти запрошенный ресурс.',
                        'description': 'Resource not found.',
                        'error': 'DiskNotFoundError'}
        self.assertNotEqual(dictionary, dict_pattern, f"Папки '{name}' на Диске нет!")
        return dictionary
