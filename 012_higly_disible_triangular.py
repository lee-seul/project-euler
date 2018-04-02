# coding: utf-8
# 012_highly_disible_triangular.py

def count_divisor(num):
	x = 2
	count = 1
	factor_list = []
	while(num!=1):
		if num % x == 0:
			factor_list.append(x)
			num = num/x
		else:
			x += 1
	factor_set = list(set(factor_list))
	for i in factor_set:
		count *= factor_list.count(i) + 1
	return count

tri_num = 1
num = 2

while(True):
	tri_num += num
	num += 1
	if count_divisor(tri_num) > 500:
#		print(tri_num)
		break
	print(count_divisor(tri_num))
		



