import requests
import pytest
import cerberus


def test_status(default_url_3):
    r = requests.get(default_url_3)

    assert r.status_code == 200 and r.encoding == "UTF-8" and r.headers["Connection"] == "keep-alive"


def test_json(default_url_3):
    r = requests.get(default_url_3 + "posts/1")
    expected_json = {'userId': {"type": "number"}, 'id': {"type": "number"},
                     'title': {"type": "string"}, 'body': {"type": "string"}}
    v = cerberus.Validator()

    assert v.validate(r.json(), expected_json)


@pytest.mark.parametrize("input_id, output_id", [(-99, "-99"), (99, "99"), (0, "0")])
@pytest.mark.parametrize("input_title, output_title",
                         [("title1", "title1"), (">_<", ">_<"), ("!@#$%", "!@#$%"), ("12345", "12345")])
def test_post_request(default_url_3, input_id, output_id, input_title, output_title):
    r = requests.post(default_url_3 + "posts", data={"title": input_title, "body": "bar", "userId": input_id})
    result = r.json()

    assert result["title"] == output_title and result["body"] == "bar" and result["userId"] == output_id


@pytest.mark.parametrize('input_id, output_id', [(1, '1'), (-10, '-10'), (0.5, '0.5')])
@pytest.mark.parametrize('input_title, output_title', [('foo', 'foo'), ('_', '_'), ('qwr', 'qwr'), ('&', '&')])
def test_put_request(default_url_3, input_id, output_id, input_title, output_title):
    r = requests.put(default_url_3 + "posts/1", data={'title': input_title, 'body': 'bar', 'userId': input_id})
    result = r.json()

    assert result['title'] == output_title and result['body'] == 'bar' and result['userId'] == output_id


@pytest.mark.parametrize("user_id", [0, 'a', 1111111, -1, "#"])
def test_user_id_negative(default_url_3, user_id):
    r = requests.get(default_url_3 + "posts", params={"userId": user_id})

    assert not r.json()
