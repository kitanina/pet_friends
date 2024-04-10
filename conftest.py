import pytest
import settings
from api.api import PetFriends
from selenium import webdriver
from faker import Faker

from ui_framework.pages.signup_page import SignUpPage

fake = Faker()


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
    return pets


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(name='main_page', scope='function')
def open_main_page(browser):
    browser.get(settings.base_url)
    return SignUpPage(browser)


@pytest.fixture(name='user_data', scope='function')
def generate_user_data():
    user_data = {'name': fake.first_name(),
                 'email': fake.email(),
                 'password': fake.password()}
    return user_data
