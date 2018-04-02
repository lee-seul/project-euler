# coding: utf-8
# pandigital_prime.py

from itertools import permutations
from lib.primes import is_prime

def make_pandigital(num):
	l = [i for i in range(1, num+1)]
	permut_list = list(permutations(l, ))
	result_list = []	
	for permutation in permut_list:
		string = ''
		for num in permutation:
			string += str(num)
		result_list.append(int(string))
	return result_list


pandigital_list = make_pandigital(7) 

pandigital_list.sort()
pandigital_list.reverse()

for pandigital in pandigital_list:
	if is_prime(pandigital):
		print(pandigital)
		break



