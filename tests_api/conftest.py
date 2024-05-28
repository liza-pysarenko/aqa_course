import random
import pytest
from backend.pets import pet_api
from http.client import HTTPException


@pytest.fixture()
def generate_random_pet_id():
    return random.randint(0, 999)


@pytest.fixture
def create_pet(generate_random_pet_id):
    payload = {
        "id": generate_random_pet_id,
        "category": {
          "id": 0,
          "name": "string"
        },
        "name": "TestPet",
        "photoUrls": [
          "string"
        ],
        "tags": [
          {
            "id": 0,
            "name": "string"
          }
        ],
        "status": "available"
    }
    response = pet_api.create_pet(payload=payload)
    return response.json()


@pytest.fixture
def clean_up_pet(generate_random_pet_id):
    yield
    response = pet_api.delete_pet(pet_id=generate_random_pet_id)
    if response.status_code != 200:
        raise HTTPException(response.text)
