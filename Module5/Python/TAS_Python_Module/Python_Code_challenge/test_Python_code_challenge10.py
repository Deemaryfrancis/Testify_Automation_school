#Create a function that converts any string value to a Sentence case,
# Then  write  a  unit  test  that  checks  the function's correctness

import pytest
from Python_code_challenge10 import convertToCapitalize

def test_lowercase_convertToCapitalize():
    string1 = "where are you going?"
    convertToCapitalize(string1)
    assert convertToCapitalize(string1) == "Where are you going?"

def test_Uppercase_convertToCapitalize():
    string2 = "WHAT IS YOUR NAME?"
    convertToCapitalize(string2)
    assert convertToCapitalize(string2) == "What is your name?"

def test_Sentencecase_convertToCapitalize():
    string3 = "what is your profession?"
    convertToCapitalize(string3)
    assert convertToCapitalize(string3) == "What is your profession?"
