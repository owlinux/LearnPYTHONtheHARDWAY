# -*- coding: utf-8 -*-
# ex15.py

from sys import argv

script, filename = argv

try:
	with open(filename) as txt:
		print("Read filename is:")
		print(txt.read())
except IOError as ioerr:
	print(str(ioerr))

custom_filename = input("읽은 싶은 파일 이름은?")
context = open(custom_filename)
print("파일 내용은:")
print(context.read())
close(context)
