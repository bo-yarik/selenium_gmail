from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from fixture.session import SessionHelper
from fixture.mail import MailHelper


class Application():
    def __init__(self, browser):
        if browser == 'Chrome':
            self.wd = Chrome(executable_path=r'C:\py\selen3\selen2\selen\drivers\win32\chromedriver.exe')

        self.session = SessionHelper(self)
        self.mail = MailHelper(self)

    def open_main_page(self):
        wd = self.wd
        wd.get("https://accounts.google.com")

    def destroy(self):
        self.wd.quit()