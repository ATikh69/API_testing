import pytest
import requests
import cerberus


def test_url_status_brewery(base_url_brewery):
    resp = requests.get(base_url_brewery + "/madtree-brewing-cincinnati")
    assert resp.status_code == 200


def test_api_json_schema(base_url_brewery):
    resp = requests.get(base_url_brewery + "/madtree-brewing-cincinnati").json()
    schema = {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'brewery_type': {'type': 'string'},
        'street': {'type': 'string'},
        'address_2': {"nullable": True, 'type': 'string'},
        'address_3': {"nullable": True, 'type': 'string'},
        'city': {'type': 'string'},
        'state': {'type': 'string'},
        'county_province': {"nullable": True, 'type': 'string'},
        'postal_code': {'type': 'string'},
        'country': {'type': 'string'},
        'longitude': {'type': 'string'},
        'latitude': {'type': 'string'},
        'phone': {'type': 'string'},
        'website_url': {'type': 'string'},
        'updated_at': {'type': 'string'},
        'created_at': {'type': 'string'}
    }
    valid = cerberus.Validator()
    assert valid.validate(resp, schema)


def test_by_city(base_url_brewery):
    resp = requests.get(base_url_brewery + f"?by_city=Cincinnati").json()
    tmparr = []
    for i in resp:
        tmp = i["city"]
        tmparr.append(tmp)
    if "Cincinnati" not in tmparr:
        result = "False"
    else:
        result = "True"
    assert result == "True"


@pytest.mark.parametrize("count", [1, 5, 10])
def test_by_city_and_img_count(base_url_brewery, count):
    resp = requests.get(base_url_brewery + f"?by_city=Cincinnati&per_page={count}").json()
    assert len(resp) == count


def test_headers(base_url_brewery):
    resp = dict(requests.get(base_url_brewery + "/random").headers)
    assert resp.get("Content-Type") == "application/json; charset=utf-8"
