# coding: utf-8
# 003_largest_prime_factor.py

def find_largest_prime(number):
	l = []
	n = 2
	while number!=1:
		if number % n == 0:
			l.append(n)
			number = number/n
		else: 
			n += 1
	return max(l)

print(find_largest_prime(600851475143))

		
