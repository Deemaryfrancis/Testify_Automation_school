# 1. Use for loop to iterate from 0 to 10
# 2. For each iteration print out "Number ", i
# 3. If the i value is equal to 2 add the continue
# 4. If the i value is equal to 8 add the break statement
#    N.B  For instruction 2, to print out Number and i, use the statement in your loop,
#         print("Number", i)

new_number = 10
for i in range(new_number):
	i += 1
	print("Number", i)
	if i == 2:
		continue
	elif i == 8:
		break
