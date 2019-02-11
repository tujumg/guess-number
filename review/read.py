data = []
count = 0 
with open('reviews.txt','r')as f:
	for line in f: 
		data.append(line)
		count += 1
		if count % 1000 == 0: #除1000等於零
			print(len(data))
print('讀取完畢',len(data),'筆資料')	 

print(data[0])
wc = {} #word_count
for d in data: #d唯一筆留言,data為清單
	words = d.split(' ')
	print(words)
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增
for word in wc:
	if wc[word] > 100 :
		print(word,wc[word]) #word 指的是key,wc[word]指的是value
print(len(wc))
while True:
	word = input('你想查什麼字？')
	if word == 'q':
		break	
	print(word,'出現過的次數為:',wc[word])
