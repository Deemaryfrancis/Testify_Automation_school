#Create  a  function  that  converts  any  string  value  to  uppercase,
# Then  write  a  unit  test  that  checks  the  function's correctness.
import pytest
from Python_code_challenge9 import convertToUpper
def test_LowerCase_convertToUpper():
    string1 = "i am a boy"
    Test1 = convertToUpper(string1)
    print(Test1)
    assert Test1 == "I AM A BOY"

def test_UpperCase_convertToUpper():
    string2 = "I AM A GIRL"
    Test2 = convertToUpper(string2)
    print(Test2)
    assert Test2 == "I AM A GIRL"

def test_SentenceCase_convertToUpper():
    string3 = "The gown is blue"
    Test3 = convertToUpper(string3)
    print(Test3)
    assert Test3 == "THE GOWN IS BLUE"
