import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.CSS_SELECTOR, """#login > div:nth-child(1) > label > input""")
    LOCATOR_PASS_FIELD = (By.CSS_SELECTOR, """#login > div:nth-child(2) > label > input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """#login > div.submit.svelte-uwkxn9 > button > span""")
    LOCATOR_ERROR_FIELD = (By.CSS_SELECTOR, """#app > main > div > div > div.error-block.svelte-uwkxn9 > h2""")
    LOCATOR_SUCCESS = (By.CSS_SELECTOR, """ #app > main > nav > ul > li.svelte-1rc85o5.mdc-menu-surface--anchor > a""")
    LOCATOR_BTN_NEW_POST = (By.CSS_SELECTOR,
                            """#app > main > div > div.actions.svelte-1e9zcmy > div.button-block.svelte-1e9zcmy""")
    LOCATOR_TITLE_NEW_POST = (By.CSS_SELECTOR, """#create-item > div > div > div:nth-child(1) > div > label > input""")
    LOCATOR_DESC_NEW_POST = (By.CSS_SELECTOR,
                             """#create-item > div > div > div:nth-child(2) > div > label > span > textarea""")
    LOCATOR_CONTENT_NEW_POST = (By.CSS_SELECTOR,
                                """#create-item > div > div > div:nth-child(3) > div > label > span > textarea""")
    LOCATOR_BTNSAVE_NEW_POST = (By.CSS_SELECTOR, """#create-item > div > div > div:nth-child(7) > div > button""")
    LOCATOR_TITLE_SAVE_POST = (By.CSS_SELECTOR, """#app > main > div > div.container.svelte-tv8alb > h1""")
    LOCATOR_CONTACT_US = (By.CSS_SELECTOR, """#app > main > nav > ul > li:nth-child(2)""")

    LOCATOR_TEXT_CONTACT_US = (By.CSS_SELECTOR, """#app > main > div > div > h1""")

    LOCATOR_CONTACT_US_NAME = (By.CSS_SELECTOR, """#contact > div:nth-child(1) > label > input""")
    LOCATOR_CONTACT_US_EMAIL = (By.CSS_SELECTOR, """#contact > div:nth-child(2) > label > input""")
    LOCATOR_CONTACT_US_CONTENT = (By.CSS_SELECTOR, """#contact > div:nth-child(3) > label > span > textarea""")
    LOCATOR_CONTACT_US_BUTTON = (By.CSS_SELECTOR, """#contact > div.submit > button""")


class OperationHelper(BasePage):
    def enter_login(self, login):
        logging.info(f'Send word "{login}" in element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(login)

    def enter_pass(self, password):
        logging.info(f'Send word "{password}" in element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(password)

    def click_login_button(self):
        logging.info(f'click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        error_text = error_field.text
        logging.info(f'we find text "{error_text}" in error field  {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return error_text

    def get_success_text(self):
        success_field = self.find_element(TestSearchLocators.LOCATOR_SUCCESS)
        success_text = success_field.text
        logging.info(f'we find text "{success_text}" in error field {TestSearchLocators.LOCATOR_SUCCESS[1]}')
        return success_text

    def click_new_post_button(self):
        logging.info(f'click button "new post"')
        self.find_element((TestSearchLocators.LOCATOR_BTN_NEW_POST)).click()

    def enter_title_new_post(self, title):
        logging.info(f'Send word "{title}" in element {TestSearchLocators.LOCATOR_TITLE_NEW_POST[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_NEW_POST)
        title_field.clear()
        title_field.send_keys(title)

    def enter_description_new_post(self, description):
        logging.info(f'Send word "{description}" in element {TestSearchLocators.LOCATOR_DESC_NEW_POST[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_DESC_NEW_POST)
        title_field.clear()
        title_field.send_keys(description)

    def enter_content_new_post(self, content):
        logging.info(f'Send word "{content}" in element {TestSearchLocators.LOCATOR_CONTENT_NEW_POST[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_NEW_POST)
        title_field.clear()
        title_field.send_keys(content)

    def click_save_new_post(self):
        logging.info(f'click  button "save post"')
        self.find_element(TestSearchLocators.LOCATOR_BTNSAVE_NEW_POST).click()

    def get_title_save_post(self):
        title_post_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_SAVE_POST, time=5)
        title_field = title_post_field.text
        logging.info(f'we find text "{title_field}" in error field{TestSearchLocators.LOCATOR_TITLE_SAVE_POST[1]}')

        return title_field

    def enter_page_contact_us(self):
        logging.info(f'click button "Contact"')
        contact_us = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US)
        contact_us.click()
        text_contact_us = self.find_element(TestSearchLocators.LOCATOR_TEXT_CONTACT_US, time=5)
        return text_contact_us.text

    def enter_contact_us_name(self, name):
        logging.info(f'Send word "{name}" in field {TestSearchLocators.LOCATOR_CONTACT_US_NAME[1]}')
        name_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_NAME)
        name_field.clear()
        name_field.send_keys(name)

    def enter_contact_us_email(self, email):
        logging.info(f'Send word "{email}" in field {TestSearchLocators.LOCATOR_CONTACT_US_EMAIL[1]}')
        email_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_EMAIL)
        email_field.clear()
        email_field.send_keys(email)

    def enter_contact_us_content(self, content):
        logging.info(f'Send word "{content}" in field {TestSearchLocators.LOCATOR_CONTACT_US_CONTENT[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_CONTENT)
        content_field.clear()
        content_field.send_keys(content)

    def click_button_contact_us(self):
        logging.info(f'click button "Contact us"')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BUTTON).click()
        time.sleep(2)

    def get_text_alert(self):
        alert = self.driver.switch_to.alert.text
        logging.info(f'get alert text "{alert}"')
        return alert