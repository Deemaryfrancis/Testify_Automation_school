#Write  a  Python  program  that  checks  if  a  string  is  a palindrome,
# Then  optionally  write  a  unit  test  to  checkyour program's correctness

import pytest

import Python_code_challenge5
from Python_code_challenge5 import Checkstring

def test_is_palindrome():
    string1 = "radar"
    Test1 = Checkstring(string1)
    assert Test1 == (string1, string1[-1::-1], "This is a palindrome")

def test_is_not_palindrome():
    string1 = "padar"
    Test2 = Checkstring(string1)
    assert Test2 == (string1, string1[-1::-1], "This is not a palindrome")

