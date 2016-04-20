# -*- coding: utf-8 -*-
# ex39.py

states = {
	"충청북도": "충북",
	"경상북도": "경북",
	"전라남도": "전남",
	"경기도": "경기",
	"강원도": "강원"
}

cities = {
	"전남": "광주",
	"강원": "원주",
	"경북": "대구"
}

cities["경기"] = "수원"
cities["충북"] = "충주"

print("-" * 20)
print("경기도에는 ", cities['경기'])
print("충청북도에는 ", cities['충북'])

print("-" * 20)
print("강원도의 약자는 ", states['강원도'])
print("경상북도의 약자는 ", states["경상북도"])

print("-" * 20)
for state, abbrev in states.items():
	print(state, abbrev)

print("-" * 20)
for abberv, city in cities.items():
	print(abberv, city)
