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

    def test_links_combo(self):

        login(self.driver)
        sleep(5)

        linksCombo = self.driver.find_element_by_class_name('links_log_form')
        assert linksCombo is not None

        sleep(3)

        links = linksCombo.find_elements_by_xpath('//*[@id="log_form_links"]/div[1]/div[2]/ul/li/a')
        assert 10 == len(links)

        secondLink = links[1]
        assert 'gazeta' in secondLink.get_attribute('href')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
