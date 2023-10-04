"""тесты для API"""
import logging

import requests
import yaml
from BaseAPI import BaseAPI

with open('testdata.yaml', encoding='utf-8') as fy:
    testdata = yaml.safe_load(fy)

s = requests.Session()


class OperatorsHelperAPI(BaseAPI):
    """методы для тестов"""

    def get_title(self, owner=None):
        """получение списка названий постов"""
        res = self.get_post(owner=owner)
        res_title = [i['title'] for i in res]
        return res_title

    def create_new_post(self):
        """создание нового поста"""
        self.create_post(testdata['title'], testdata["description"], testdata['content'])