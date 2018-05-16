from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time


def waiting_for(wd, find_by, elem, retries=60):
    find_dict = {'name': By.NAME, 'class_name': By.CLASS_NAME, 'css_selector': By.CSS_SELECTOR}
    try:
        WebDriverWait(wd, retries).until(EC.visibility_of_element_located((find_dict[find_by], elem)))
    except TimeoutException:
        print
        "Timed out waiting for page to load"


def click_if_exist(wd, selector):
    time.sleep(2)
    try:
        wd.find_elements_by_css_selector(selector)[0].click()
    except:
        print('letters doesnt exist')