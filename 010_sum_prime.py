# coding: utf-8
# sum_prime.py

from lib.primes import is_prime
			

				

def sum_prime(num):
	result = 2
	for i in range(3, num, 2):
		if is_prime(i):
			result += i
	return result


print(sum_prime(2000000))


