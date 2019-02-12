import time 
import progressbar

data = []
count = 0 
bar = progressbar.ProgressBar(max_value = 1000000)
with open('reviews.txt','r')as f:
	for line in f: 
		data.append(line)
		count += 1
		bar.update(count)
		if count % 1000 == 0: #除1000等於零
			print(len(data))
print('讀取完畢',len(data),'筆資料')	 

sum_length = 0	
for d in data:
	sum_length += len(d)     
print('平均留言長度為',sum_length/len(data))

new = []
for d in data:#d(每一筆留言)是字串,data是清單
     if len(d)<100:
     	new.append(d)
print('一共有',len(new),'筆留言小於一百字') 
print(new[2])

good = []
for e in data:
	if 'good' in e: #True or False
		good.append(e)  
print('一共有',len(good),'提到good')

print(data[0])

#文字的計數
start_time = time.time()
wc = {} #word_count
for d in data: #d唯一筆留言,data為清單
	words = d.split(' ')
	
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增
for word in wc:
	if wc[word] > 1000000 :
		print(word,wc[word]) #word 指的是key,wc[word]指的是value
end_time = time.time()
print('花了',end_time - start_time,'秒')
print(len(wc))
while True:
	word = input('你想查什麼字？')
	if word == 'q':
		break	
	print(word,'出現過的次數為:',wc[word])
