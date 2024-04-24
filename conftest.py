import pytest
from store_facade import StoreFacade


@pytest.fixture(name='store')
def store():
    return StoreFacade()


@pytest.fixture(name='store')
def request(request):
    return StoreFacade()
