# coding:utf-8
# 009_special_pythagorean_triplet.py

from math import sqrt

def find_special_pythagorean(num):
	k = 0
	result = 0
	for i in range(1, int(num/2)):
		for j in range(1, int(num/2)):
			k = i**2 + j **2
			if sqrt(k) == int(sqrt(k)) and i + j + sqrt(k) == num:
				result = i*j*sqrt(k)
	return result


print(find_special_pythagorean(1000))
