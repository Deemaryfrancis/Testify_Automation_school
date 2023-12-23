#1. Create a test case that compares two strings
#2. Create another test case that compares different numbers

#Use any unit testing framework from this week's lessons.

import pytest
from python_Task26 import comparestring
from python_Task26 import comparenumbers

def test_strings_are_different():
    string1 = "where are you going?"
    string2 = "where are you?"
    comparestring(string1, string2)
    assert comparestring(string1, string2) == "String1 is not equal to String2"

def test_strings_are_thesame():
    string1 = "where are you going?"
    string2 = "where are you going?"
    comparestring(string1, string2)
    assert comparestring(string1, string2) == "String1 is equal to String2"

def test_numbers_are_different():
    Number1 = "25"
    Number2 = 25
    assert comparenumbers(Number1, Number2) == "Number1 is not equal to Number2"

def test_numbers_are_thesame():
    Number1 = 25
    Number2 = 25
    assert comparenumbers(Number1, Number2) == "Number1 is equal to Number2"



