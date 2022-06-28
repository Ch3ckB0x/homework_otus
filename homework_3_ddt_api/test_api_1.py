import cerberus
import requests
import pytest


def test_api_status(default_url_1):
    res = requests.get(default_url_1 + 'dog-api/')
    assert res.status_code == 200
    assert res.encoding == 'UTF-8'
    assert res.headers['content-type'] == 'text/html; charset=UTF-8'


def test_api_validate_json(default_url_1):
    res = requests.get(default_url_1 + 'api/breeds/image/random')
    if res.status_code == 200:
        schema = {
            "message": {"type": "string"},
            "status": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(res.json(), schema)
    else:
        assert False


@pytest.mark.parametrize("link", ["https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg",
                                  "https://images.dog.ceo/breeds/hound-afghan/n02088094_12563.jpg",
                                  "https://images.dog.ceo/breeds/hound-afghan/n02088094_4837.jpg"])
def test_api_by_breed(default_url_1, link):
    res = requests.get(default_url_1 + 'api/breed/hound/images')
    if link in res.json()["message"]:
        assert True
    else:
        assert False


@pytest.mark.parametrize('dog,breed', [('bulldog', ['boston', 'english', 'french']),
                                       ('borzoi', []),
                                       ('australian', ['shepherd']),
                                       ('mountain', ['bernese', 'swiss'])],
                         ids=['bulldog', 'borzoi', 'australian', 'mountain'])
def test_api_content_json(default_url_1, dog, breed):
    res = requests.get(default_url_1 + 'api/breeds/list/all')
    if res.status_code == 200:
        assert res.json()['message'][dog] == breed
    else:
        assert False


@pytest.mark.parametrize('breed', ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'],
                         ids=['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'])
def test_api_content_json1(default_url_1, breed):
    res = requests.get(default_url_1 + 'api/breed/hound/list')
    if res.status_code == 200:
        assert breed in res.json()['message']
    else:
        assert False
