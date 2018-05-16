# -*- coding: utf-8 -*-

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from snippets.tools import *




class MailHelper:
    def __init__(self, app):
        self.app = app

    def new_letter(self):
        wd = self.app.wd
        waiting_for(wd, 'class_name', 'aic')
        wd.find_element_by_class_name('aic').click()
        waiting_for(wd, 'name', 'to')

    def fill_recipients(self, recipient):
        wd = self.app.wd
        waiting_for(wd, 'name', 'to')
        wd.find_element_by_name('to').click()
        wd.find_element_by_name('to').clear()
        wd.find_element_by_name('to').send_keys(recipient)
        wd.find_element_by_name('to').send_keys(Keys.TAB)

    def fill_subject(self, subject):
        wd = self.app.wd
        wd.find_element_by_name('subjectbox').click()
        wd.find_element_by_name('subjectbox').clear()
        wd.find_element_by_name('subjectbox').send_keys(subject)

    def fill_message(self, message):
        wd = self.app.wd
        textbox = wd.find_elements_by_xpath("//*[@role='textbox']")[0]
        textbox.click()
        textbox.clear()
        textbox.send_keys(message)

    def send_letter(self):
        wd = self.app.wd
        send_button = wd.find_elements_by_css_selector(".T-I.J-J5-Ji.aoO")
        send_button[0].click()

    def open_letter(self, mail):
        wd = self.app.wd
        waiting_for(wd, 'name', mail, 80)
        wd.find_element_by_name(mail).click()
        time.sleep(10)

    def get_text(self, selector):
        wd = self.app.wd
        waiting_for(wd, 'css_selector', selector)
        text = wd.find_element_by_css_selector(selector).text
        #text = wd.find_elements_by_xpath("//*[@class='{0}']".format(cls))[0].text
        return text

    def answer_letter(self, answer):
        wd = self.app.wd
        wd.find_element_by_css_selector(".ams.bkH").click()
        wd.find_element_by_css_selector(".Am.aO9.Al").click()
        wd.find_element_by_css_selector(".Am.aO9.Al").send_keys(answer)

    def receive_letter(self):
        wd = self.app.wd
        waiting_for(wd, 'css_selector', ".yW")
        wd.find_element_by_css_selector(".yW").click()

    def delete_all_letters(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".T-Jo-auh").click()
        click_if_exist(wd, ".ar9.T-I-J3.J-J5-Ji")









