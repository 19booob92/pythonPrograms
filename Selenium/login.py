from time import sleep
from selenium import webdriver
from testbase import MAIN_PAGE
from testbase import open_main_page
from testbase import login

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = open_main_page()
        assert 'Logowanie' in self.driver.page_source

    def test_login(self):

        login(self.driver)
        sleep(3)

        assert 'Informacje systemowe' in self.driver.page_source

    def test_login_fail(self):
        login(self.driver, password = 'fake pass')
        sleep(5)

        assert 'Informacje systemowe' not in self.driver.page_source

        loginMessageBox = self.driver.find_element_by_id('loginMessage')
        assert 'Błędny login' in loginMessageBox.get_attribute('innerHTML')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
