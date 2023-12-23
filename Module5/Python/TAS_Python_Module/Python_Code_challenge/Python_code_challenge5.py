#Write  a  Python  program  that  checks  if  a  string  is  a palindrome,
# Then  optionally  write  a  unit  test  to  checkyour program's correctness

def Checkstring(string1):
    string2 = string1[-1::-1]
    print("Not reversed string: ", string1)
    print("Reversed string: ", string2)
    if string2 == string1:
        Answer = ("This is a palindrome")
        print(Answer)
    else:
        Answer = ("This is not a palindrome")
        print(Answer)
    return (string1, string2, Answer)
Checkstring("civic")

