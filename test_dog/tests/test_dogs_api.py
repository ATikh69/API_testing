import pytest
import requests
import cerberus
import re


def test_url_status_dogs(base_url_dog):
    resp = requests.get(base_url_dog + "/breeds/image/random")
    assert resp.status_code == 200


def test_api_json_schema(base_url_dog):
    resp = requests.get(base_url_dog + "/breeds/image/random").json()
    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
    valid = cerberus.Validator()
    assert valid.validate(resp, schema)


def test_message_status(base_url_dog):
    resp = requests.get(base_url_dog + "/breeds/image/random").json()
    assert resp.get("status") == "success"


def test_sub_breeds(base_url_dog):
    resp = requests.get(base_url_dog + "/breed/hound/list").json()
    assert resp["message"] == ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker']



@pytest.mark.parametrize("count", [1, 5, 10, 50])
def test_several_rnd_img(base_url_dog, count):
    resp = requests.get(base_url_dog + f"/breeds/image/random/{count}").json()
    assert len(resp["message"]) == count


@pytest.mark.parametrize("breed", ['hound', 'mastiff', 'retriever'])
def test_by_breed_img2(base_url_dog, breed):
    resp = requests.get(base_url_dog + f"/breed/{breed}/images").json()
    tmparray = []
    rls = None
    for i in resp["message"]:
        tmp = re.match(f'https://images.dog.ceo/breeds/{breed}', i)
        tmparray.append(tmp)
    if None in tmparray:
        rls = "False"
    else:
        rls = "True"
    assert rls == "True"
