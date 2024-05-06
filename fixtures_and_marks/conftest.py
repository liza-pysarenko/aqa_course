import pytest
from fixtures_and_marks.store_facade import StoreFacade


@pytest.fixture(name='store')
def store():
    return StoreFacade()


@pytest.fixture()
def store_with_request(request):
    store_facade = StoreFacade()
    request.cls.store = store_facade
    return store_facade


class TestStore:

    @pytest.mark.usefixtures(name='store')
    def test_add_and_show_catalog(self, store):
        store.add_phone_to_catalog("Google Pixel 8", 700)
        store.add_phone_to_catalog("OnePlus 10T 5G", 500)
        assert len(store.show_catalog()) == 2
