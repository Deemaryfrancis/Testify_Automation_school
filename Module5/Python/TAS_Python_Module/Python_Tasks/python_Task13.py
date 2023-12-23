#1. Create a function that prints out "Hello World"
#2. Invoke the same function in it own body
#3. Invoke the function outside the function block
# N.B: Take note of the function invoke and put the Python whitespace rule in min

def greet():
    print("Hello Word")
    greet()
greet()