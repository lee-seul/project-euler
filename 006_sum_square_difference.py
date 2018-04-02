# coding: utf-8
# 006_sum_square_difference.py

def sum_square_diff(num):
	square_sum = 0
	sum_square = 0
	for i in range(1, num+1):
		square_sum += i**2
		sum_square += i
	sum_square = sum_square**2
	return(sum_square - square_sum)

print(sum_square_diff(100))
