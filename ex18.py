# -*- coding: utf-8 -*-
# ex18.py

def print_two(*args):
	arg1, arg2 = args
	print("실행인자: %r, 실행인자: %r" % (arg1, arg2))

def print_two_again(arg1, arg2):
	print("실행인자: %r, 실행인자 %r" % (arg1, arg2))

def print_one(arg1):
	print("실행인자: %r" % arg1)

def print_none():
	print("아무것도 받지 않음")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

