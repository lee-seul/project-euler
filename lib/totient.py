# coding: utf-8
# totient.py

from lib.gcd_lcm import gcd

def phi(num):
	result = 0
	for i in range(1, num+1):
		if gcd(num, i) == 1:
			result += 1

	return result

