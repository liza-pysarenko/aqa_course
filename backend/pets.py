from backend.api import APIInterface


class PetsInterface(APIInterface):

    def create_pet(self, payload: dict):
        return self._post('pet/', json=payload)

    def delete_pet(self, pet_id: int):
        return self._delete(f'pet/{pet_id}')

    def find_pet_by_id(self, pet_id: int, **kwargs):
        return self._get(f'pet/{pet_id}', **kwargs)

    def update_pet(self, payload: dict):
        return self._put('pet/', json=payload)


pet_api = PetsInterface()
