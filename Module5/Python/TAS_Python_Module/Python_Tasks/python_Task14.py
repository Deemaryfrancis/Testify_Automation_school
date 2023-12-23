name = "   TAutomation Module 3A   "
print(name.upper())


#Others
#Size - displays the total length of the string
size = len(name)
print("Size:", size)

#Upper - Covert string to upper case
upper_value = name.upper()
print(upper_value)

#Lower - Covert string to lower case
lower_value = name.lower()
print(lower_value)

#Capitalize - Convert string to sentence case
capitalized_value = name.capitalize()
print(capitalized_value)

#Count - count the occurence of a value in a string
Count_value = name.count("a")
print(Count_value)

Count_value1 = name.count("A")
print(Count_value1)

Count_value2 = name.count("Module")
print(Count_value2)

# Find - get the position of  value in a string
for_position = name.find("3A")
print(for_position)

#Index -get the position of  value in a string
for_index = name.index("3A")
print(for_index)

#Strip - remove excess space in the beginning and end of a string
stripped_name = name.strip()
print(stripped_name)

#rstrip - remove excess spaces at the end of the string
rstripped_name = name.rstrip()
print(rstripped_name)

#lstrip - rstrip - remove excess spaces at the beginning of the string
lstripped_name = name.lower()
print(lstripped_name)

#split - split a string to array using a specify value
splitted_name = name.split("tion")
print(splitted_name)

#Format - format the specified value of a string
#named format

unformatted_one ="My name is {name}, I am a {occupation}"
formatted_one = unformatted_one.format(name="Deemary", occupation="Developer")
print("Named formatter: ", formatted_one)

#indexed format
unformatted_index ="My name is {0}, I am a {1}"
formatted_index = unformatted_index.format("Deemary", "Developer")
print("indexed formatter: ", formatted_index)

#indexed format
unformatted_unindex ="My name is {}, I am a {}"
formatted_unindex = unformatted_unindex.format("Deemary", "Developer")
print("unindexed formatter: ", formatted_unindex)
