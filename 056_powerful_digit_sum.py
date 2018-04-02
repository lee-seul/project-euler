# coding: utf-8
# 056_powerful_digit_sum.py



def digit_sum(num):
	num_list = list(str(num))
	total = 0
	for i in num_list:
		total += int(i)
	return total


max_value = 0

for i in range(1, 100):
	for j in range(1, 100):
		num = i**j
		if digit_sum(num) > max_value:
			max_value = digit_sum(num)

print(max_value)
			

