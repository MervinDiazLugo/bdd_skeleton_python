import logging
import os
from src.functions.GlobalConfig import Config

# Directorio Base
basedir = os.path.abspath(os.path.join(__file__, "../.."))
DateFormat = '%d/%m/%Y'
HourFormat = "%H%M%S"


def before_all(self):
    # print('1- Before all')
    pass


def before_feature(self, feature):
    # print(f'2- Before Feature: {feature}')
    pass


def before_scenario(self, scenario):
    # print(f'3- Before Scenario: {scenario}')
    if Config.Environment == 'Dev':
        print("Hola Chicos Dev")
    if Config.Environment == 'Test':
        print("Hola Chicos Test")


def before_step(self, step):
    # print(f'4- Before step {step}')
    pass


def after_step(self, step):
    # print(f'4.1- after step {step}')
    pass


def before_tag(self, tag):
    '''if tag == "Test":
        print("Hola, ejecutaste el tag test")
'''
    pass


def after_all(self):
    # print('5- after all')
    pass


def after_feature(self, feature):
    # print(f'6- after feature {feature}')
    pass


def after_scenario(self, scenario):
    # print(f'6- after scenario {scenario}')
    pass
