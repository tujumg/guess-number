import random
r = random. randint(1,100)
count = 0
while True:
	num = input('輸入一個數字')
	num = int(num)
	count = count + 1
	if num == r:
		print('恭喜答對了	')
		print('這是你猜的第',count,'次')
		break
	elif num < r:
		print('比答案小')
	elif num > r:
		print('比答案大')
	print('這是你猜的第',count,'次')