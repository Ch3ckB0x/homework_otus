import requests
import pytest


def test_status(default_url_2):
    r = requests.get(default_url_2)

    assert r.status_code == 200 and r.encoding == "ISO-8859-1" and r.headers["Content-Encoding"] == "gzip"


@pytest.mark.parametrize("key", ["id", "name", "brewery_type", "street", "address_2", "address_3", "city", "state",
                                 "county_province", "postal_code", "country", "longitude", "latitude", "phone",
                                 "website_url", "updated_at", "created_at"],
                         ids=["id", "name", "brewery_type", "street", "address_2", "address_3", "city", "state",
                              "county_province", "postal_code", "country", "longitude", "latitude", "phone",
                              "website_url", "updated_at", "created_at"])
def test_check_key_single_brewery(default_url_2, key):
    r = requests.get(default_url_2 + "breweries/madtree-brewing-cincinnati")

    if key in r.json():
        assert True
    else:
        assert False


@pytest.mark.parametrize("key", ["id", 'name'],
                         ids=["id", "name"])
def test_variability_keys(default_url_2, key):
    r = requests.get(default_url_2 + "breweries?by_dist=38.8977,77.0365")
    count = len(r.json())
    id_list = set()
    for i in r.json():
        id_list.add(i[key])

    assert len(id_list) == count


@pytest.mark.parametrize("expected_name",
                         ["Banjo Brewing", "Dirt Road Brewing", "Dented Face Brewing Company", "Bent Shovel Brewing"])
def test_content_json_all(default_url_2, expected_name):
    r = requests.get(default_url_2 + "breweries")
    name_list = set()
    for i in r.json():
        name_list.add(i["name"])

    assert expected_name in name_list


def test_check_len_list(default_url_2):
    r = requests.get(default_url_2 + "breweries?page=15&per_page=3")
    if len(r.json()) == 3:
        assert True
    else:
        assert False
