import pytest
import requests
import cerberus
import re


def test_url_status_jph(base_url_jph):
    resp = requests.get(base_url_jph + "/users")
    assert resp.status_code == 200


@pytest.mark.parametrize("id", [1, 3, 10])
def test_user_id(base_url_jph, id):
    resp = requests.get(base_url_jph + f"/users/{id}").json()
    assert resp["id"] == id


def test_photo_jph_check(base_url_jph):
    resp = requests.get(base_url_jph + "/photos/2").json()
    assert resp["thumbnailUrl"] == "https://via.placeholder.com/150/771796"


def test_post_check(base_url_jph):
    json = {"userId": 1, "title": "test title", "body": "test body"}
    resp = requests.post(base_url_jph + "/posts", json)
    assert resp.status_code == 201


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_post_id_in_comments(base_url_jph, post_id):
    resp = requests.get(base_url_jph + f"/comments?postId={post_id}").json()
    tmparray = []
    rls = None
    for i in resp:
        str1 = i["postId"]
        if str1 == post_id:
            tmparray.append("True")
        else:
            tmparray.append("False")
    if "False" in tmparray:
        rls = "False"
    else:
        rls = "True"
    assert rls == "True"
