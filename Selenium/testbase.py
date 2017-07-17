from selenium import webdriver
from time import  sleep
from properties import LOGIN
from properties import MAIN_PAGE
from properties import PASS

def open_main_page():
    webDriver = webdriver.Chrome('./chromedriver')
    webDriver.get(MAIN_PAGE)
    sleep(3)
    return webDriver

def login(webDriver, login=LOGIN, password=PASS):
    login_box = webDriver.find_element_by_name('username')
    login_box.send_keys(login)

    password_box = webDriver.find_element_by_name('password')
    password_box.send_keys(password)

    login_btn = webDriver.find_element_by_class_name('login_btn')
    login_btn.click()
