# Create  a  function  that  calculates  the  power  of  a  number.
# Then  write  a  unit  test  to  check  the  correctness  of  the function.

from Python_code_challenge2 import power_number

def test_powerToNumber():
    number1 = 2
    power1 = 3
    assert power_number(number1, power1) == 8

def test_Division_not_powerToNumber():
    number2 = 2
    power2 = 3
    assert power_number(number2, power2) != (number2/power2)

def test_multiply_not_powerToNumber():
    number3 = 2
    power3 = 3
    assert power_number(number3, power3) != (number3*power3)

def test_Subtraction_not_powerToNumber():
    number4 = 2
    power4 = 3
    assert power_number(number4, power4) != (number4-power4)
