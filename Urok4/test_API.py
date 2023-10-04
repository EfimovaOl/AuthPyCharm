""" модуль с тестами API"""
import yaml
from testPageAPI import OperatorsHelperAPI

with open('testdata.yaml', encoding='utf-8') as fy:
    testdata = yaml.safe_load(fy)


def test_get_post_in_title():
    """получение чужого поста по наименованию"""
    test_api = OperatorsHelperAPI()
    res_title = test_api.get_title(owner='notMe')

    assert testdata['search_title'] in res_title


def test_create_new_post():
    """создание поста и проверка что он создался"""
    test_api = OperatorsHelperAPI()
    test_api.create_new_post()
    res_title = test_api.get_title()

    assert testdata['title'] in res_title