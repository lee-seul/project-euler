# coding: utf-8
# 007_prime_10001st.py

from lib.primes import is_prime

def find_prime(num):
	prime_list = []
	n = 1
	while(len(prime_list)!=num):
		n+=1
		if is_prime(n):
			prime_list.append(n)
	return prime_list[-1]
		
		
print(find_prime(10001))


		
