# -*- coding: utf-8 -*-
# ex8.py

formatter = "%s %s %s %s"

print(formatter % (1, 2, 3, 4))
print(formatter % ("하나", "둘", "셋", "넷"))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
	"난 이게 있죠.",
	"지금 막 써 주신 그것.",
	"하지만 '노래'하지 않아요.",
	"그러니가 잘자요."
	))

formatter2 = "%r %r %r %r"

print(formatter2 % (
	"i had this thing.",
	"that you could type up right.",
	"but it didn't sing.",
	"so i said goodnight"
	))
