# -*- coding: utf-8 -*-
# ex32.py

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pear', 'apricot']
change = [1, 'ten coin', 2, 'one hundred won', 3, 'five hundred won']

for number in the_count:
	print("number is %d" % number)

for fruit in fruits:
	print("fruit type is %s" % fruit)

for i in change:
	print("changes is %s", i)

elements = []

for j in range(0, 6):
	print("add list. %d" % j)
	#elements.append(j)

elements.extend(range(0,10))

for j in elements:
	print("element is %d" % j)
