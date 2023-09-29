import pytest
import testdata
import yaml
from module import Site

site = Site(testdata['address'])

with open('testdata.yaml') as fy:
    testdata = yaml.safe_load(fy)


#@pytest.fixture(autouse=True)
#def setUp():
 #   site = Site(testdata['address'])


@pytest.fixture()
def selector_login():
    return "css", """#login > div:nth-child(1) >label > input"""

@pytest.fixture()
def selector_password():
    return "css", """#login > div:nth-child(2) > label > input"""

@pytest.fixture()
def selector_button():
    return "css", """#login > div:nth-child(2) > label > input"""

@pytest.fixture()
def selector_error():
    return "css", """#login > div:nth-child(2) > label > input"""

@ pytest.fixture()
def result_error():
    return '401'

@pytest.fixture()
def selector_hello():
    return "css", """#app > main > nav > ul > li.svelte-1rc85o5.mdc-menu-surface--anchor > a"""

@pytest.fixture()
def result_hello():
    return f'Hello, {testdata["username"]}'

@pytest.fixture()
def selector_button_new_post():
    return "css", """#app > main >div > div.actions.svelte-1e9zcmy > div.button-block.svelte-1e9zcmy"""

@pytest.fixture()
def selector_title_new_post():
    return "css", """#create-item > div >div > div:nth-child(1) > label >input"""

@pytest.fixture()
def selector_description_new_post():
    return "css", """#create-item > div > div > div:nth-child(2) > div >label > span > textarea"""

@pytest.fixture()
def selector_content_new_post():
    return "css", """#create-item > div > div > div:nth-child(3) > div >label > span > textarea"""
@pytest.fixture()
def selector_buttonsave_new_post():
    return "css", """#create-item > div > div > div:nth-child(7) > div >button"""

@pytest.fixture()
def selector_title_save_post():
    return "css", """#app > main > div > div.container.svelte-tv8alb > h1"""
