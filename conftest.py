import pytest
import settings
from api.api import PetFriends


@pytest.fixture(name='token', scope='function')
def get_token():
    pf = PetFriends()
    email = settings.email
    password = settings.password
    token = pf.get_get_token(email, password).json().get('key')
    return token


@pytest.fixture(name='pet_data')
def pet_data():
    return [
        {'name': 'Alice', 'age': 30, 'animal_type': 'HR'},
        {'name': 'Bob', 'age': 30, 'animal_type': 'Tech'}
    ]


@pytest.fixture(name='create_delete_pet', scope='function')
def create_pet(token: str, pet_data: list):
    pf = PetFriends()
    pets = []
    for pet in pet_data:
        response = pf.post_create_pet(auth_key=token,
                                      name=pet['name'],
                                      animal_type=pet['animal_type'],
                                      age=pet['age']).json()
        pets.append(response)
    yield pets
    pet_list = pf.get_list_of_pets(token).json()['pets']
    pet_ids = [pet['id'] for pet in pets]
    for pet in pet_list:
        if pet['id'] in pet_ids:
            pf.delete_pet(token, pet['id'])
