import requests


def test_check_url(default_url, status_code):
    response = requests.get(default_url)
    assert response.status_code == status_code
