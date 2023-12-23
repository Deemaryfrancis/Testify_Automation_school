#Using the OOP feature Inheritance, create a class Animal with the method sound() and
# then create a Cat and Dog class that inherits from the Animal class.
# The Cat and Dog class should override the sound class and print a different sound.


class Animal:

    def __init__(self, sound):
        self.sound = sound

#animal = Animal("Sounding bass")
#print (animal.sound)

#For Cat
class Cat(Animal):
    pass
cat = Cat("mew")
print("Sound a cat makes is: ", cat.sound)

#For Dog
class Dog(Animal):
    pass
dog = Dog("woof")
print("Sound a dog makes is: ", dog.sound)
