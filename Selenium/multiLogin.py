from time import sleep
from selenium import webdriver
from testbase import MAIN_PAGE
from testbase import open_main_page
from testbase import login
import csv
import unittest

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
            for row in csv.reader(data, delimiter = ';'):
                login(self.driver, row[0], row[1])
                sleep(3)

                if 'Informacje systemowe' not in self.driver.page_source:
                    self.writer('login: ' + row[0], 'haslo: ' + row[1])

    def writer(self, login, password):
        with open('accounts_with_error.txt', 'a') as output:
            outputContent = login + ' ' + password + '\n'
            output.write(outputContent)


if __name__ == "__main__":
    unittest.main()
