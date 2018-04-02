# coding: utf-8
# 044_pentagon_numbers.py

from lib.X_number import is_pentagon, num_5

pentagon_list = []

n= 1

Not_found = True
while(Not_found):
	pentagon_list.append(num_5(n))
	for j in range(2, len(pentagon_list)-1):
		if is_pentagon(pentagon_list[-1] + pentagon_list[j]) and is_pentagon(pentagon_list[-1] - pentagon_list[j]):
			print(abs(pentagon_list[j] - pentagon_list[-1]))
			Not_found = False
	n += 1
				





