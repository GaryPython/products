#讀取檔案 
products = []
with open('products2.csv', 'r', encoding = 'utf-16') as f:
	for line in f:
		if '商品,價格' in line:
			continue#繼續
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
			break
	price = input('請輸入商品價格：')
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]		
	products.append([name, price])
print(products)	

#印出所有購買紀錄
for p in products:
	print(p)
	print(p[0], '的價格是', p[1])

#字串可加乘
#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
