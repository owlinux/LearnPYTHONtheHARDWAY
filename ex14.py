# -*- coding: utf-8 -*-
# ex14.py

from sys import argv

script, user_name = argv
prompt = "> "

print("안녕 %s, 나는 %s 스크립트야." % (user_name, script))

print("몇가지 물어볼께")
print("%s, 나를 좋아해?" % user_name)
like = input(prompt)

print("%s 어디에 살아?" % user_name)
live = input(prompt)

print("%s, 어떤 종류의 컴퓨터를 갖고 있어?" % user_name)
computer = input(prompt)

print("""
좋아, 나를 좋아하냐는 질문에는 '%s'.
%s에 살아. 어딘지는 모르겠지만.
그리고 '%s' 컴퓨터를 가졌어. 멋져.
""" % (like, like, computer))
