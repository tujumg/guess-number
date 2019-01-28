import random
start = input('輸入起始值')
end = input('輸入範圍結束值')
start = int(start)
end = int(end) 
r = random. randint(start,end)
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