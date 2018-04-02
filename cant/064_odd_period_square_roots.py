# coding: utf-8
# 064_odd_period_square_roots.py

from math import sqrt


def square_roots(num):
	num_list = [int(sqrt(num))]	
	
	
	
	
	a = sqrt(num) - num_list[0]
	b = 1 
	 = sqrt(num) + num_list[0]
	b = int(n * a) + 1
	num_list.append(int(a/b))
	x = 1 
	while():
		tmp = a
		a = b 
		b = tmp


print(square_roots(23))







