import pytest


@pytest.fixture(scope='session')
def default_url_1(request):
    return request.config.getoption('--url', default='https://dog.ceo/')


@pytest.fixture(scope='session')
def default_url_2(request):
    return request.config.getoption('--url', default='https://api.openbrewerydb.org/')


@pytest.fixture(scope='session')
def default_url_3(request):
    return request.config.getoption('--url', default='https://jsonplaceholder.typicode.com/')
