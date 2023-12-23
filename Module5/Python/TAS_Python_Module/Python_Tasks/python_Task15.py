#1. Declare a list with any value and number of item/element
#2. Print the list in console
#3. Sort the list
#4. Print the list in console again

Tech_Career = ["Developer", "Project Manager", "UI/UX"]
Tech_Career.sort()
print(Tech_Career)
print("Sort-ascending: ", Tech_Career)
Tech_Career.sort(reverse=True)
print("Sort-descending: ", Tech_Career)

#Append - Add new item(s) to the end of the list
Tech_Career.append("Data Analyst")
print(Tech_Career)

#Insert - Insert new items at a specific position in the list
Tech_Career.insert(2, "Scrum Master")
print("insert: ", Tech_Career)

#Pop - Remove an Item from a specified position
Tech_Career.pop(4)
print("Pop-0: ", Tech_Career)
Tech_Career.pop()
print("Pop: ", Tech_Career)

#Remove - Remove an item by value
Tech_Career.remove("Scrum Master")
print(Tech_Career)

#Count - Counts the number of occurence of item in the list
Tech_Career.append("Full Stack Developer")
Count_Tech_Career = Tech_Career.count("Developer")
print(Count_Tech_Career)

#len - Count the total number of items in a list
Length_Tech_career = len(Tech_Career)
print("len: ", Length_Tech_career)

#Copy - Return the copy of that List
Copy_Tech_career = Tech_Career.copy()
print("Copy: ", Copy_Tech_career)

#Reverse - Reverse the order of item in a list
before_reverse = Copy_Tech_career
Tech_Career.reverse()
print("before reverse: ", before_reverse)
print("after reverse: ", Tech_Career)

#Sort - Sort the list of items in a list either by ascending or descending order

#Extend - add the content of the specified list to our current list
Tech_Career.extend(["Business analyst", "Cyber Security Analyst", "Test Automation Engineer"])
print(Tech_Career)

#Clear - Removes all Items in the list
Tech_Career.clear()
print("clear: ", Tech_Career)
