#1. Create an anonymous function that prints out "Hello World"
#2. Invoke/call the function


def accept(cb):
    cb("Hello World")

greet = lambda : print("Hello World")
greet()

accept(lambda x : print(x))