import pytest
from store_facade import StoreFacade


@pytest.fixture
def store():
    return StoreFacade()


@pytest.mark.parametrize("model, price", [("iPhone 15", 1500), ("Google Pixel 7", 700)])
def test_add_phone_to_catalog(store, model, price):
    phone = store.add_phone_to_catalog(model, price)
    assert phone.model == model
    assert phone.price == price
    assert phone in store.show_catalog()


@pytest.mark.smoke
def test_remove_phone_from_catalog(store):
    store.add_phone_to_catalog("iPhone 12", 1000)
    removed_phone = store.remove_phone_from_catalog("iPhone 12")
    assert removed_phone is not None
    assert removed_phone.model == "iPhone 12"
    assert removed_phone not in store.show_catalog()


def test_add_and_show_catalog(store):
    store.add_phone_to_catalog("Google Pixel 8", 700)
    store.add_phone_to_catalog("OnePlus 10T 5G", 500)
    assert len(store.show_catalog()) == 2


@pytest.mark.parametrize("model, price", [("Xiaomi 14 Ultra", 1220), ("Honor Magic 6 Pro", 900)])
def test_add_phone_to_catalog_with_params(store, model, price):
    store.add_phone_to_catalog(model, price)
    phones = store.show_catalog()
    assert any(phone.model == model and phone.price == price for phone in phones)


@pytest.mark.catalog_operations
def test_add_and_remove_phone(store):
    store.add_phone_to_catalog("iPhone 13", 1300)
    assert len(store.show_catalog()) == 1
    store.remove_phone_from_catalog("iPhone 13")
    assert len(store.show_catalog()) == 0


@pytest.mark.catalog_operations
def test_clear_catalog(store):
    store.add_phone_to_catalog("Samsung Galaxy S22", 1200)
    assert len(store.show_catalog()) == 1
    store.catalog.phones.clear()
    assert len(store.show_catalog()) == 0
