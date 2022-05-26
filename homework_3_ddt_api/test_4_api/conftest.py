import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="http://ya.ru", help="Url for test api location")
    parser.addoption("--status_code", default=200, help="Status code for test api location")


@pytest.fixture()
def default_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def status_code(request):
    return int(request.config.getoption("--status_code"))
