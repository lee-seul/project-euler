# coding: utf-8
# 062_cubic_permutations.py

from itertools import permutations as pm

def num_to_list(num):
	digit_list = [int(i) for i in str(num)]
	digit_list.sort()
	return digit_list

cubic_list = [num_to_list(i**3) for i in range(1000, 10000)]

	

for i in cubic_list:
	if cubic_list.count(i) == 5:
		result = i
		break

for i in range(1000, 10000):
	if num_to_list(i**3) == result:
		print(i**3)
		break


