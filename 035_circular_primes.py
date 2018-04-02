# coding: utf-8
# 035_circular_primes.py

from lib.primes import is_prime


def is_circular_prime(num):
	num = str(num)
	length = len(num)
	for i in range(length):
		if not is_prime(int(num[i:]+num[:i])):
			return False
	return True

prime_list = []


for i in range(2, 1000001):
	if is_circular_prime(i):
		prime_list.append(i)


print(len(prime_list))



