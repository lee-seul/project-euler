# coding: utf-8
# permutation_combinations.py


def factorial(num):
	result = 1
	if num == 0:
		return 1
	else:
		for i in range(1, num+1):
			result *= i
		return result


def combination(num, r):
	if r == 0:
		return 1
	else:
		if num - r == 0:
			result = factorial(num)/factorial(r)
		else:
			result = factorial(num)/(factorial(r)*factorial(num-r))
		
		return result



