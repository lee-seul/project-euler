# coding: utf-8
# 070_totient_permutation.py

from lib.primes import is_prime
from lib.totient import phi

def is_permutation(num1, num2):
	return sorted(list(str(num1))) == sorted(list(str(num2)))


n = 9999999
while(True):
	print(n)
	if is_prime(n) and is_permutation(phi(n),n):
		print(n)
		break
	n-= 1

