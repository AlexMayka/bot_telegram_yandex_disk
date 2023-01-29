import requests
import json


with open('venv/get_request_parameters.json') as json_file:
    dict_request_param = json.load(json_file)

URL = dict_request_param['URL']
TOKEN = dict_request_param['TOKEN']
headers = dict_request_param['headers']


def get_information_about_disk():
    URL_get_info_about_disk = URL.replace("/resources", '')
    req_get_information = requests.get(URL_get_info_about_disk, headers=headers)
    req_get_information.raise_for_status()
    print(f'Получение информаии, статус - {req_get_information.status_code}')
    print(req_get_information.json())


def create_folder_in_disk(path_to_the_new_folder):
    URL_create_folder = f'{URL}?path={path_to_the_new_folder}'
    print(URL_create_folder)
    req_create_folder = requests.put(URL_create_folder, headers=headers)
    print(f'Создание папки, статус - {req_create_folder.status_code}')  # Статус 409 - существует


def get_a_list_of_files():
    URL_get_a_list_files = f'{URL}/files'
    headers_get_a_list_of_files = headers
    headers_get_a_list_of_files['preview_crop'] = 'false'
    print(URL_get_a_list_files)
    req_create_folder = requests.get(r'https://cloud-api.yandex.net/v1/disk/resources/files', headers=headers_get_a_list_of_files)
    print(req_create_folder.json())
    # for i in req_create_folder.json()['items']:
    #     print(i)


if __name__ == "__main__":
    get_information_about_disk(get_information_about_disk())
