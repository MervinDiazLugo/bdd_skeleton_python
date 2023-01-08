# -*- coding: utf-8 -*-

import time

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.functions.GlobalConfig import Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OpcionesChrome
import datetime
diaGlobal = time.strftime("%Y-%m-%d")  # formato aaaa/mm/dd
horaGlobal = time.strftime("%H%M%S")  # formato 24 houras
Scenario = {}


class Commons(Config):

    def __init__(self):
        self.var = "Hola Mundo"

    def sumas (self, number1, number2):
        self.result = int(number1)+ int(number2)
        return self.result

    def resultscheck(self, checking):
        assert self.result == int(checking), f'el resultado no es el correcto, se esperaba {checking} pero se recibio {self.result}'

##########################################################################
    ##############   -=_INICIALIZAR DRIVERS_=-   #############################
    ##########################################################################
    def open_browser(self, URL=Config.URL, navegador=Config.NAVEGADOR):
        self.ventanas = {}
        print("----------------")
        print(navegador)
        print(Config.basedir)
        print("---------------")


        if navegador == ("CHROME"):
            options = OpcionesChrome()
            options.add_argument('start-maximized')
            self.driver = webdriver.Chrome(chrome_options=options,
                                           executable_path=Config.basedir + "\\drivers\\chromedriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("CHROME_headless"):
            options = OpcionesChrome()
            options.add_argument('headless')
            options.add_argument('--start-maximized')
            options.add_argument('--lang=es')
            self.driver = webdriver.Chrome(chrome_options=options)
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("FIREFOX"):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("CHROME_GRID"):
            options = OpcionesChrome()
            options.add_argument('--start-maximized')
            options.add_argument('--lang=es')
            options.add_argument('window-size=1920x1080')
            self.driver = driver = webdriver.Remote(desired_capabilities=options.to_capabilities())
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        elif navegador != ("CHROME_headless") and navegador != ("CHROME") and navegador != ("FIREFOX"):
            print("----------------")
            print("Define el DRIVER")
            print("----------------")
            pytest.skip("Define el DRIVER")
            exit

    def tearDown(self, test="pass"):
        print("Se cerrará  el DRIVER")
        self.driver.quit()
        if test == "fail":
            testFail = False
            msj = self.msj
            if self.msj == "":
                assert testFail == True, "Test Fail"
            else:
                assert testFail == True, msj

    def textDateEnvironmentReplace(self, text):
        meDateFormat = '%d/%m/%Y'
        if text == 'today':
            self.today = datetime.date.today()
            text = self.today.strftime(Config.DateFormat)

        if text == 'yesterday':
            self.today = datetime.date.today() - datetime.timedelta(days=1)
            text = self.today.strftime(Config.DateFormat)

        if text == 'LastMonth':
            self.today = datetime.date.today() - datetime.timedelta(days=30)
            text = self.today.strftime(Config.DateFormat)

        if text == 'format_today':
            self.today = datetime.date.today()
            text = self.today.strftime(meDateFormat)

        if text == 'format_yesterday':
            self.today = datetime.date.today() - datetime.timedelta(days=1)
            text = self.today.strftime(meDateFormat)

        if text == 'format_LastMonth':
            self.today = datetime.date.today() - datetime.timedelta(days=30)
            text = self.today.strftime(meDateFormat)

        print(text)
        return text

    def implicit_wait_visible(self, locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located(*locator))
        except TimeoutException:
            print("Element no visible")

    def check_if_elelent_is_visible(self, locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            print("Element no visible")
            return False

    def setText(self, locator, text):
        try:
            self.driver.find_element(*locator).send_keys(text)
        except ValueError:
            print("Cannot set text on element")
