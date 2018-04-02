# coding: utf-8
# 004_largest_palindrome_product.py

num = 0
l = []

for i in range(100,1000):
	for j in range(100,1000):
		num = i*j
		if num > 100000:
			num = str(num)
			if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
				l.append(num)


print(max(l))
		
