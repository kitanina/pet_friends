import base64

import pytest
from api.api import PetFriends

pf = PetFriends()
photo_path = 'C:/Users/alena/PycharmProjects/study/tests/images/b9c47ef70bff06613d397abfce02c6e7.jpg'


def upload_photo_for_pets(created_pets, token):
    for pet in created_pets:
        res = pf.post_set_photo(auth_key=token,
                                pet_id=pet['id'],
                                pet_photo_path=photo_path)
        return res


def check_created_pets(created_pets, pets_from_system):
    system_pet_ids = {pet['id'] for pet in pets_from_system}

    for pet in created_pets:
        if pet['id'] not in system_pet_ids:
            return False
    return True


def update_pet_info(created_pets, token):
    pets = []
    for pet in created_pets:
        response = pf.put_update_pet_info(auth_key=token,
                                          pet_id=pet['id'],
                                          name='Test update',
                                          animal_type='Test update',
                                          age='Test update').json()
        pets.append(response)
    return pets


def pet_photo_to_base64(pet_photo_path):
    with open(pet_photo_path, 'rb') as pet_photo:
        encoded_pet_photo = base64.b64encode((pet_photo.read()))
        return encoded_pet_photo


def compare_photo(encoded_pet_photo, received_base64_string):
    local_photo = encoded_pet_photo
    received_base64 = received_base64_string.split(',', 1)[-1]
    return local_photo == received_base64


def check_created_pets(created_pets, pets_from_system):
    for pet in created_pets:
        if pet not in pets_from_system:
            return False
    return True


def check_updated_pets(created_pets, updated_pets):
    for updated_pet in updated_pets:
        # Находим соответствующего питомца из исходного списка по id.
        original_pet = next((pet for pet in created_pets if pet['id'] == updated_pet['id']), None)

        # Проверяем, что питомец был найден, и что его данные действительно обновились.
        if original_pet:
            # Проверяем, что данные изменились согласно условиям.
            if original_pet['name'] != updated_pet['name'] == 'Test update' and \
                    original_pet['animal_type'] != updated_pet['animal_type'] == 'Test update' and \
                    original_pet['age'] != updated_pet['age'] == 'Test update':
                continue  # Этот питомец успешно обновлен, продолжаем проверять остальных.
            else:
                # Если условия для какого-либо питомца не выполнились, возвращаем False.
                return False
        else:
            # Если не нашли питомца по ID, что-то пошло не так.
            return False

    # Если проверка прошла для всех питомцев, возвращаем True.
    return True


@pytest.mark.flaky(reason='innt-1020')
def test_pet_friends(token, create_delete_pet):
    token = token

    created_pets: list = create_delete_pet
    pets_from_system: list = pf.get_list_of_pets(auth_key=token).json()
    assert check_created_pets(created_pets, pets_from_system)

    received_base64_string = upload_photo_for_pets(token=token, created_pets=created_pets).json()['res']['pet_photo']
    local_encoded_pet_photo = pet_photo_to_base64(photo_path)
    assert compare_photo(local_encoded_pet_photo, received_base64_string)

    updated_pets = update_pet_info(token=token, created_pets=created_pets)['pets']
    assert check_updated_pets(created_pets, updated_pets)

    deleted_pet = pf.delete_pet(token,)
