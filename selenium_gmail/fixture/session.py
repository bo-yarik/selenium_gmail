import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from snippets.tools import *


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_name("identifier").click()
        wd.find_element_by_name("identifier").clear()
        wd.find_element_by_name("identifier").send_keys(login)
        wd.find_element_by_id("identifierNext").click()
        time.sleep(2)
        waiting_for(wd, 'name', 'password')
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_id("passwordNext").click()
        time.sleep(2)

    def logout(self):
        wd = self.app.wd
        wd.implicitly_wait(5)
        wd.find_element_by_link_text("Logout").click()