# coding: utf-8
# 037_truncatable_primes.py

from lib.primes import is_prime

prime_list = []

def truncate_prime(num):
	num = str(num)
	for i in range(len(num)):
		if not is_prime(int(num[i:])):
			return False
	for i in range(len(num), 0, -1):
		if not is_prime(int(num[:i])):
			return False
	return True

num = 11	
while(len(prime_list)<11):
	if truncate_prime(num):
		prime_list.append(num)
	num += 1

print(sum(prime_list))


