# OOP Inheritance
#1. Create a class called Human
#2. Add an attribute leg_count with the value of 4
#3. Add a method called get_gender() that returns "Unknown" in the Human class
#4. Create another class called Man that extends Human

class Human:
    leg_count = 4
    can_walk = "True"

    def get_gender(self):
        print("unknown")

class Man(Human):
    name = "Thomas"

Test = Human()
Test.get_gender()


sex = Man()
print(sex.name, sex.leg_count, sex.can_walk)
sex.get_gender()