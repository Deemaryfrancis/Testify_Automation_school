#Introduction to OOP - Object Oriented Programming
#1. Create a class called Human
#2. Initialize the class

class Human:
    name = "Mary"
    gender = "Female"
    def fetch_name_gender(self):
        return self.name + ":" + self.gender
# object: instaniate the class
test = Human()
print(test.name, test.gender, test.fetch_name_gender())
