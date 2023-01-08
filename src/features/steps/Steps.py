# -*- coding: utf-8 -*-
from behave import *
from src.functions.Commons import Commons
from src.pages.google import googlePage

use_step_matcher("re")


class StepsDefinitions():

    @given("I add the values (.*) and (.*)")
    def step_impl(context, number1, number2):
        Commons.sumas(context, number1, number2)

    @then("Add result is (.*)")
    def step_impl(context, resultcheck):
        Commons.resultscheck(context, resultcheck)


    @given("I am in the main site")
    def step_impl(context):
        Commons.check_if_elelent_is_visible(context, googlePage.searchBox)


    @step("I set search box with value (.*)")
    def step_impl(context, value):
       Commons.setText(context, googlePage.searchBox, value)