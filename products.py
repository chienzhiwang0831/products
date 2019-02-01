products = []
while True:
	name = input('商品: ')
	if name == 'q':
		break
	price = int(input('價格: '))
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價是', p[1])