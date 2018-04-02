# coding: utf-8
# 058_spiral_primes.py

from lib.primes import is_prime

spiral_list = [1]
n = 1
plus = 2
i = 0
count = 0
while(True):
	value = spiral_list[i] + plus
	spiral_list.append(value)
	i += 1
	if i % 4 == 0:
		for num in spiral_list[-4:]:
			if is_prime(num):
				count += 1
		result = count/i
		print(result)
		if result >= 0.1:
			n += 2
			plus += 2
		else:
			print(n)
			break





