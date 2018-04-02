# coding: utf-8
# 034_digit_factorials.py

from lib.permutation_combinations import factorial


def digit_factorial_sum(num):
	digit_sum  = sum([factorial(int(i)) for i in list(str(num))])
	return num == digit_sum


result = 0

for i in range(3, 2540161):
	if digit_factorial_sum(i):
		result += i

print(result)



