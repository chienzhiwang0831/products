import os #operating system
# 讀取檔案
def read_products(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 讓使用者輸入
def input_products(products):
	while True:
		name = input('商品: ')
		if name == 'q':
			break
		price = int(input('價格: '))
		products.append([name, price])
	print(products)
	return products

# 印出購買記錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_products(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):# 檢查是否有這檔案
		print('準備開啟檔案')
		products = read_products(filename)
	else:
		print('找不到檔案')	
	products = input_products(products)
	print_products(products)
	write_products('products.csv', products)

main()