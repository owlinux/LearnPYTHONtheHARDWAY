# -*- coding: utf-8 -*-
# ex21.py

def add(a, b):
	print("덧셈 %d + %d" % (a, b))
	return a + b

def subtract(a, b):
	print("뺄셈 %d - %d" % (a, b))
	return a - b

def multiply(a, b):
	print("곱셈 %d * %d" % (a, b))
	return a * b

def divide(a, b):
	print("나눗셈 %d / %d" % (a, b))
	return a / b

print("함수만으로 계산해 봅시다.!")

age = add(30 , 6)
height = subtract(74, 4)
weight = multiply(90, 2)
iq = divide(400, 2)

print("나이 %d, 키 %d, 몸무게 %d, IQ %d" % (age, height, weight, iq))


print("문제가 있어요!!!")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("결과: ", what, "손으로 계산할 수 있나요?")
