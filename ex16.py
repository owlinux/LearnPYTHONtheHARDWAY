# -*- coding: utf-8 -*-
# ex16.py

from sys import argv

script, filename = argv

print("%r 파일을 지우려 합니다." % filename)
print("취소하려면 CTRL-C을 누르세요.")
print("진행하려면 리턴을 누르세요.")

input("?")

print("파일을 여는 중...")
try:
	with open(filename, "w") as file:
		print("파일을 지웁니다.")
		#file.truncate()

		print("이제 세 줄에 들어갈 내용을 묻겠습니다.")

		line1 = input("1줄 : ")
		line2 = input("2줄 : ")
		line3 = input("3줄 : ")
		
		print("이제 파일을 씁니다.")
		file.write(line1 + "\n")
		file.write(line2 + "\n")
		file.write(line3 + "\n")

except IOError as ioerr:
	print(str(ioerr))

