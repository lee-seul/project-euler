# coding: utf-8
# primes.py

from math import sqrt

def is_prime(num):
	if num > 1:
		for i in range(2, int(sqrt(num))+1):
			if num % i == 0:
				return False
		return True
	else:
		return False



def find_primes_factor(num):
	l = []
	n = 2
	while num!=1:
		if num % n == 0:
			l.append(n)
			num = num/n
		else:
			n += 1
	return l




