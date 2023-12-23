#OOP Methods
#1. Create a class called Human
#2. Add an attribute leg_count with the value of 4
#3. Add another attribute can_walk with the value of True
#4. Create a method called get_description, the method should print "This is human"
#5.Create another method that return the leg count, the name of the method is your choice

class Human:
    leg_count = 4
    can_walk = True

    def get_description(self):
        print("This is human")
    def get_leg_count(self, count):
        self.leg_count = count

Test = Human()
Test.get_description()
Test.get_leg_count(5)
print("Leg Count: ", Test.leg_count)
