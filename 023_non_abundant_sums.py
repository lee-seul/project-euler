# coding: utf-8
# 023_non-abundant_sums.py


def is_abundant(num):
	divisor_sum = 0
	for i in range(1, int((num/2)+1)):
		if num % i == 0:
			divisor_sum += i
	if num < divisor_sum:
		return True
	return False

abundant = [] 
for i in range(2, 28124):
	if is_abundant(i):
		abundant.append(i)

result = 0
for x in range(1, 28124):
	for abun in abundant:
		if x > abun:
			if x - abun in abundant:
				break
		else:
			result += x
			break

print(result)



