import pytest
import requests
import yaml

S = requests.Session()

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def user_login():
   result = S.post(url=data['url'], data={'username': data['login'], 'password': data['password']})
   response_json = result.json()
   print(response_json)


@pytest.fixture()
def user_login1():
    result = S.get(url=data['address'], headers={'X-Auth-Token': 'token'}, params={'owner': 'notMe'}).json()['data']
    print(result)

@pytest.fixture()
def post_title():
    return(post_title)

@pytest.fixture()
def post():
    obj_data = S.post(url=data['address'], headers={'X-Auth-Token': 'token'},
                      data={'username': 'login', 'password': 'password',
                            'title': 'newTitle', 'description': 'Anything',
                            'content': 'we will see'})
    return obj_data.json()['description']
