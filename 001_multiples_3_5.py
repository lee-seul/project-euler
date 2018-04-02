# coding: utf-8
# 001_multiples_3_5.py

def multiple_3_5(number):
	total = []
	for i in range(number):
		if i % 3 == 0 or i % 5 == 0:
			total.append(i)
	return sum(set(total))	


print(multiple_3_5(1000))
