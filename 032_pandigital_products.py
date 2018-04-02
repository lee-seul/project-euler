# coding: utf-8
# 032_pandigital_products.py

def is_pandigital_multiple(num1, num2):
	pandigital = [str(i) for i in range(1, 10)]
	l = list(str(num1) + str(num2) + str(num1*num2))
	l.sort()
	return pandigital == l 

result_list = []
for x in range(1, 100):
	for y in range(100, 2000):
		if is_pandigital_multiple(x, y):
			result_list.append(x*y)
	
print(sum(set(result_list)))


