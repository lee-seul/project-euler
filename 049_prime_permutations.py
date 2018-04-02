# coding: utf-8
# 049_prime_permutations.py

from itertools import permutations as pm
from lib.primes import is_prime

def is_permutations(num1, num2, num3):
	num1 = list(str(num1))
	num2 = list(str(num2))
	num3 = list(str(num3))
	num1.sort()
	num2.sort()
	num3.sort()
	return num1 == num2 and num2 == num3

primes = []

for i in range(1000, 10000):
	if is_prime(i):
		primes.append(i)

	
sub = 0
for x in primes:
	for y in primes:
		sub = x - y
		if sub > 0 and x+sub in primes:
			if is_permutations(y, x, x+sub):
				print(y, x, x+sub)



