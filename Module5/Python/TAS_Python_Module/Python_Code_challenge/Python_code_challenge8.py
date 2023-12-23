#Create a program that prints out the even numbers in an array.
# Sample array:
# a. [1, 2, 3, 4, 5, 6]
# b. [ 34, 2, 9, 91, 19,401, 0 ]

def number(arraynumber):
    for i in arraynumber:
        if i % 2 == 0:
            print(i, " - is an even number")
            pass
    return i

number([ 1, 2, 3, 4, 5, 6 ])