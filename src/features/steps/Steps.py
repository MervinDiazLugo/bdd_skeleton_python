# -*- coding: utf-8 -*-
from behave import *
from src.functions.Functions import Functions

use_step_matcher("re")


class StepsDefinitions():

    @given("I add the values (.*) and (.*)")
    def step_impl(context, number1, number2):
        Functions.sumas(context, number1, number2)

    @then("Add result is (.*)")
    def step_impl(context, resultcheck):
        Functions.resultscheck(context, resultcheck)
