# -*- coding: utf-8 -*-
# ex38.py

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("잠깐 아직 목록에 10개가 들어 있지 않으니 한 번 고쳐 봅시다.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("add: ", next_one)
	stuff.append(next_one)
	print("이제 남은 항목은 %d" % len(stuff))

print("한번 볼까요?", stuff)

print("이 걸로 무언가 해봅시다.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
#print(join(' ', stuff))
