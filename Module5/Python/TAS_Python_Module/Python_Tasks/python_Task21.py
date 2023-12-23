#OOP POlymorphism - OOP
#1. Create a class called Human
#2. Add an attribute leg_count with the value of 4
#3. Add a method called get_gender() that returns "Unknown" in the Human class
#4. Create another class called Man that extends Human
#5. Create another class called Woman that extends Human
#6. In the class, Man create the method get_gender() which should return "man"
#7. In the class, Woman create the method get_gender() which should return "woman"
#8. Instantiate the Man and Woman class


class Human:
    leg_count = 4
    can_walk = "True"

    def get_gender(self):
        print("unknown")

class Man(Human):
    def get_gender(self):
        print("Male")

class Woman(Human):
    def get_gender(self):
        print("Female")

human = Human()
human.get_gender()

man = Man()
man.get_gender()

woman = Woman()
woman.get_gender()