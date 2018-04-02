# coding: utf-8
# 020_factorial_digit_sum.py

def factorial(num):
	result = 1
	for i in range(1, num+1):
		result *= i
	return result
	

def digit_sum(num):
	total = 0
	num = str(num)
	for i in num:
		total += int(i)
	return total
	
print(digit_sum(factorial(100)))


