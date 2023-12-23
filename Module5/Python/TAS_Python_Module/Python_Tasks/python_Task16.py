#1. Declare a dictionary with any key-value pair of items/elements
#2. Print the dictionary in console
#3. Update the dictionary with two different key-value pair items
#4. Print the dictionary in console again

team_mate = {
    "UI/UX": "Ololade",
    "Frontend Developer": "Anthony",
    "QA analyst": "Mary"
}
print("dictionary: ", team_mate)
team_mate.update({"PM": "Francisca", "Data Anaylst": "Antonia"})
print(team_mate)


#get - To fetch the value using a specify key word
Team_UI = team_mate.get("UI/UX")
print("get: ", Team_UI)

#items - return the list of the key-value pair of a dictionary as a tuple
#tuple - is a list that is immutable and created with a round bracket
team_mate_items = team_mate.items()
print("items", team_mate_items)

#keys - retun the list of keys of a dictionary
team_mate_keys = team_mate.keys()
print("keys", team_mate_keys)

#values - return the values as a list
team_mate_values = team_mate.values()
print("value: ", team_mate_values)

#pop - remove a key -value pairs using the specific key
team_mate.pop("UI/UX")
print("pop: ", team_mate)

#popitem - remove the last key-value pairs from a dictionary
team_mate.popitem()
print("popitem", team_mate)

#copy - return a copy of a dictionary
copied_team_mate = team_mate.copy()
print("copy: ", copied_team_mate)

#clear - removes all items from a dictionary
team_mate.clear()
print("clear: ", team_mate)
print(copied_team_mate)