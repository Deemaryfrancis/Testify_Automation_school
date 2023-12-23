#Create a program that prints out the odd numbers in anarray.
# Sample array:
# a. [1, 2, 3, 4, 5, 6]
# b. [ 34, 2, 9, 91, 19,401, 0 ]

def number(arraynumber):
    for i in arraynumber:
        if i % 2 != 0:
            print(i, " - is an odd number")
            pass
    return i

number([ 34, 2, 9, 91, 19,401, 0 ])
