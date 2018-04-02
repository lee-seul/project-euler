# coding: utf-8
# 027_quadratic_primes.py

from math import fabs

def check_prime(num):
	num = int(fabs(num))
	for i in range(2, num):
		if num % i == 0:
			return False
	return True


result_ex = 0
x = 0 
result = 0
for i in range(-999, 1000):
#	print(i)
	for j in range(-999, 1000):
		n = 0
		while(True):
			result_ex = (n**2)+(i*n)+j
			if check_prime(result_ex):
				n+=1
			else:
				break
		if n > x:
			x = n
			result = i * j

print(result)


