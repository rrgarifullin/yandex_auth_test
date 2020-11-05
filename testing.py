from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep


class YaAuth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/Руслан/PycharmProjects/netology/chromedriver/chromedriver')

    def test_auth(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')
        self.assertIn('Авторизация', driver.title)
        login = driver.find_element_by_id('passp-field-login')
        login.send_keys('')           #введите логин
        login.send_keys(Keys.RETURN)
        sleep(0.5)
        password = driver.find_element_by_id('passp-field-passwd')
        password.send_keys('')      #введите пароль
        password.send_keys(Keys.RETURN)
        sleep(1)
        self.assertIn('Яндекс.Паспорт', driver.title, msg='Неверный логин или пароль')

    def tearDown(self):
        self.driver.close()