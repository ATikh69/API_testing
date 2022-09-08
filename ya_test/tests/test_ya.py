import requests


def test_ya(base_url_ya, default_status_code):
    resp = requests.get(base_url_ya + "/sfhfhfhfhfhfhfhfh")
    assert resp.status_code == default_status_code
