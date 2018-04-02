# coding: utf-8
# 046_goldbachs_other_conjecture.py

from lib.primes import is_prime

def is_goldbachs_number(num):
	try:
		if num % 2 == 0:
			raise ValueError
		else:
			if is_prime(num):
				return True
			else:
				n = 2
				x = 1
				while(True):
					c = n*(x**2)
					if is_prime(num-c):
#						print(num-c, c)
						return True
					elif num <= c:
						return False
					else:
						x += 1
	except ValueError:
		print("num should be even.")

num = 35
Not_found = True
while(Not_found):
	if not is_goldbachs_number(num):
		Not_found = False
		print(num)
	else:
		num += 2
	
