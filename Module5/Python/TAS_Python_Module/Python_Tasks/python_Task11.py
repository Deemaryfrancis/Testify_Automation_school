#1. Create a function that accepts two numbers, adds the numbers and prints out the result in the console.
#2. Create a function that return the string value "Testify Python"
#3. Invoke/call the two functions

def number(num1, num2):
    sum_number = num1 + num2
    print(sum_number)

number(2,3)

def string_Testify(name):
    word = name
    return word
words = string_Testify("Testify Python")
print(words)


def check_number(number):
    if number > 5:
        return
    print("Number:", number)

    check_number(1)
    check_number(2)
    check_number(5)
    check_number(7)
    check_number(9)

