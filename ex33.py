# -*- coding: utf-8 -*-
# ex33.py

numbers = []

def addList(count):
	"""
	j = 0
	while j < count:
		print("i is %d in top" % j)
		#count += 1
		numbers.append(j)

		j += 1
		print("Number is ", numbers)
		print("i is %d in bottom" % j)
	"""
	for j in range(0, count):
		print("j is %d in top" % j)
		numbers.append(j)

		print("Number is ", numbers)
		print("j is %d in bottom" % j)
addList(10)

print("Number: ")
for num in numbers:
	print(num)
