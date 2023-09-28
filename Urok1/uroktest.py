import pytest
import requests
import yaml

S = requests.Session()

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

def user_login():
   result = S.post(url=data['url'], data={'username': data['login'], 'password': data['password']})
   response_json = result.json()['token']
   print(response_json)

user_login()

def test_step(user_login, post_title):
    result = S.get(url=data['address'], headers={'X-Auth-Token': user_login}, params={"owner": "notMe"}).json()['data']
    result_title = [i['title'] for i in result]
    print(result)
    assert post_title in result_title, 'test_step FAIL'

def test_step1(post):
    assert 'Anything' in post, 'test_step FAIL'




