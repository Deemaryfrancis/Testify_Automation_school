#1. Create a test case that compares two strings
#2. Create another test case that compares different numbers

#Use any unit testing framework from this week's lessons.

def comparestring(string1,string2):
    if string1 == string2:
        Strvalue = "String1 is equal to String2"
        print(Strvalue)
        return Strvalue
    else:
        Strvalue = "String1 is not equal to String2"
        print(Strvalue)
        return Strvalue


comparestring("boy is good", "girl is good")

def comparenumbers(Number1, Number2):
    if Number1 == Number2:
        Numvalue = "Number1 is equal to Number2"
        print(Numvalue)
        return Numvalue
    else:
        value = "Number1 is not equal to Number2"
        print(value)
        return value

comparenumbers("25", 25)
