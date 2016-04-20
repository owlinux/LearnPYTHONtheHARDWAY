# -*- coding: utf-8 -*-
# ex17.py

from sys import argv
from os.path import exists

script, from_to, to_file = argv

print("%s에서 %s로 복사합니다." % (from_to, to_file))

try:
	with open(from_to) as f:
		data = f.read()
		print("입력 파일의 사이즈는 %d bytes" % len(data))

		print("출력 파일이 존재하나요? %s", exists(to_file))
		
		print("계속 하시려면, 엔터를, 취소하려면 CTRL-C를 누르세요")
		input()

		with open(to_file, "w") as output_file:
			output_file.write(data)

			print("좋습니다. 완료하였습니다.")

except IOError as ioerr:
	print(str(ioerr))
