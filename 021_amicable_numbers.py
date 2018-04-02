# coding: utf-8
# 021_amicable_numbers.py

def sum_divisors(num):
	total = 0
	for i in range(1, num):
		if num % i ==0:
			total += i
	return total 

result = 0
for i in range(2, 10001):
	a = sum_divisors(i)
	if sum_divisors(a) == i and a != i:
		result+=i

print(result)



