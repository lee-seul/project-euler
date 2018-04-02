# coding: utf-8
# 005_smallest_multiple.py

from lib.primes import is_prime

x = 1
for i in range(2, 21):
	if is_prime(i):
		x *= i		


def find_smallest(num):
	for i in range(1, 21):
		if num % i != 0:
			return False
	return True

x += 10 # u'20으로 나누어 지려면 끝 자리가 20이여야 하기때문 x=9699690

while(True):
#	print(x)
	if find_smallest(x):
		print(x)
		break
	else:
		x += 20


	
