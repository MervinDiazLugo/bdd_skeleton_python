# -*- coding: utf-8 -*-

import time
from src.functions.GlobalConfig import Config

diaGlobal = time.strftime("%Y-%m-%d")  # formato aaaa/mm/dd
horaGlobal = time.strftime("%H%M%S")  # formato 24 houras
Scenario = {}


class Functions(Config):

    def __init__(self):
        self.var = "Hola Mundo"

    def sumas (self, number1, number2):
        self.result = int(number1)+ int(number2)
        return self.result

    def resultscheck(self, checking):
        assert self.result == int(checking), f'el resultado no es el correcto, se esperaba {checking} pero se recibio {self.result}'
