# -*- coding: utf-8 -*-
# ex20.py

from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print(line_count, f.readline())

try:
	with open(input_file) as current_file:
		print("파일 전체를 출력해봅시다.")
		print_all(current_file)

		print("이번에는 테이프처럼 되갑아 봅시다.")
		rewind(current_file)

		print("세줄을 채워봅시다.")

		current_line = 1
		print_a_line(current_line, current_file)
		
		current_line += 1
		print_a_line(current_line, current_file)

		current_line += 1
		print_a_line(current_line, current_file)
except IOError as ioerr:
	print(str(ioerr))
