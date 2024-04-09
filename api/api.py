import json
from typing import BinaryIO
import requests

from tools.decorators import log_api_call


class PetFriends:
    base_url = 'https://petfriends.skillfactory.ru/'

    @log_api_call
    def post_create_pet(self, auth_key: str, name: str, animal_type: str, age: int):
        headers = {'auth_key': auth_key}
        data = {'name': name,
                'animal_type': animal_type,
                'age': age}
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        return res

    @log_api_call
    def get_get_token(self, email: str, password: str):
        headers = {'email': email,
                   'password': password}
        res = requests.get(self.base_url + 'api/key', headers=headers)
        return res

    @log_api_call
    def get_list_of_pets(self, auth_key: str, filter: str = ''):
        headers = {'auth_key': auth_key}
        filter = {'filter': filter}
        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        return res

    @log_api_call
    def post_add_new_info(self, auth_key: str, name: str, animal_type: str, age: str, pet_photo: BinaryIO):
        headers = {'auth_key': auth_key}
        data = {'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': pet_photo}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        return res

    @log_api_call
    def post_set_photo(self, auth_key: str, pet_id: str, pet_photo_path: str):
        headers = {'auth_key': auth_key}
        with open(pet_photo_path, 'rb') as photo_file:
            files = {'pet_photo': photo_file}
            res = requests.post(self.base_url + f'/api/pets/set_photo/{pet_id}', headers=headers, files=files)
        return res

    @log_api_call
    def delete_pet(self, auth_key: str, pet_id: str):
        headers = {'auth_key': auth_key}
        res = requests.delete(self.base_url + f'api/pets/{pet_id}', headers=headers)
        return res

    @log_api_call
    def put_update_pet_info(self, auth_key: str, pet_id: str, name=None, animal_type=None, age=None):
        headers = {'auth_key': auth_key}
        params = {'pet_id': pet_id}
        data = {'name': name,
                'animal_type': animal_type,
                'age': age}
        res = requests.put(self.base_url + f'api/pets/{params["pet_id"]}', headers=headers, data=data)
        return res