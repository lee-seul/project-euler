# coding: utf-8
# 051_prime_digit_replacement.py

from lib.primes import is_prime

prime_list = []
for num in range(100000, 10000000):
	if is_prime(num):
		prime_list.append(num)



