import logging
import os
from src.functions.GlobalConfig import Config

# Directorio Base
basedir = os.path.abspath(os.path.join(__file__, "../.."))
DateFormat = '%d/%m/%Y'
HourFormat = "%H%M%S"


def before_all(self):
    pass


def before_feature(self, feature):
    pass


def before_scenario(self, scenario):

    if Config.Environment == 'Dev':
        print("Hola Chicos Dev")

    if Config.Environment == 'Test':
        print("Hola Chicos Test")


def before_step(self, step):
    pass


def before_tag(self, tag):
    pass


def after_all(self):
    pass


def after_feature(self, feature):
    pass


def after_scenario(self, scenario):
    pass


def after_step(self, step):
    pass






