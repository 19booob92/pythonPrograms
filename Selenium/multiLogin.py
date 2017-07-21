from time import sleep
from selenium import webdriver
from testbase import MAIN_PAGE
from testbase import open_main_page
from testbase import login
from testbase import logout
import csv
import unittest

LOGIN_IDX = 0
PASS_IDX = 1
DELIMITER = ';'

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = open_main_page()
        assert 'Logowanie' in self.driver.page_source

    def test_login(self):

        self.iterateFile()

    def tearDown(self):
        self.driver.close()

    def iterateFile(self):
        with open('hasla.csv', "r") as data:
            for row in csv.reader(data, delimiter = DELIMITER):
                login(self.driver, row[LOGIN_IDX], row[PASS_IDX])
                sleep(8)

                if 'Informacje systemowe' not in self.driver.page_source:
                    self.writer('login: ' + row[LOGIN_IDX], 'haslo: ' + row[PASS_IDX])
                else:
                    logout(self.driver)
                    sleep(3)
                    self.driver = open_main_page()
                    sleep(3)

    def writer(self, login, password):
        with open('accounts_with_error.txt', 'a') as output:
            outputContent = login + ' ' + password + '\n'
            output.write(outputContent)


if __name__ == "__main__":
    unittest.main()
