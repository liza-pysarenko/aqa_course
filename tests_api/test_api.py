from backend.pets import pet_api


def test_create_pet(generate_random_pet_id, clean_up_pet):
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
    assert response.status_code == 200


def test_get_pet(create_pet, clean_up_pet):
    response = pet_api.find_pet_by_id(pet_id=create_pet['id'])
    assert response.status_code == 200


def test_update_pet(generate_random_pet_id, clean_up_pet):
    payload = {
        "id": generate_random_pet_id,
        "category": {
          "id": 0,
          "name": "string"
        },
        "name": "TestPet_modified",
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
    response = pet_api.update_pet(payload=payload)
    assert response.status_code == 200


def test_delete_pet(create_pet):
    response = pet_api.delete_pet(pet_id=create_pet['id'])
    assert response.status_code == 200
