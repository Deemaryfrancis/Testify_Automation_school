#1. Create a class called Utilities
#2. Create a static method called print_name which accepts a parameter, and prints out the parameter.
#3. Invoke the static method print_name()

#You can use any of the two methods to create your static methods.

class Utilities:
    def print_age(age):
        return age

    @staticmethod
    def print_name(name):
        return name

print(Utilities.print_name("Mary"))
Utilities.print_age = staticmethod(Utilities.print_age)
print(Utilities.print_age(23))










