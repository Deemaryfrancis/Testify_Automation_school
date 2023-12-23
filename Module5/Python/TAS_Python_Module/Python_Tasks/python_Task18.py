# OOP Attributes
# 1. Create a class called Human
#2. Add an attribute leg_count with the value of 4
#3. Add another attribute can_walk with value of True
# Optionally you can instantiate the class and prints out the leg_count and can_walk attributes

class Human:
    leg_count = 4
    can_walk = True

# Constructor: A method that is invoked when initializing our class
    #def __init__(self, name):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

Person1 = Human("Thomas", "Male")
Person2 = Human("Priscillia", "Female")
print("Person1: ", Person1.name, Person1.gender)
print("Person2: ", Person2.name, Person2.gender)
print("Person1: leg count is", str(Person1.leg_count) + " and can walk is", str(Person1.can_walk))
print("Person2: leg count is", Person2.leg_count)
