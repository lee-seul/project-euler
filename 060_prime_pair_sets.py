# coding: utf-8
# prime_pair_sets.py

from lib.primes import is_prime

def is_prime_pair(prime1, prime2):
	prime1 = str(prime1)
	prime2 = str(prime2)
	if is_prime(int(prime1+prime2)) and is_prime(int(prime2+prime1)):
		return True
	else:
		return False

prime_list = []
for i in range(2, 10000):
	if is_prime(i):
		prime_list.append(i)

prime_pair_list = []

for prime1 in prime_list:
	prime_pair = [prime1]
	for prime2 in prime_list:
		if is_prime_pair(prime1, prime2):
			if len(prime_pair) == 1:
				prime_pair.append(prime2)
			elif len(prime_pair) == 2:
				if is_prime_pair(prime_pair[1], prime2):
					prime_pair.append(prime2)
			elif len(prime_pair) == 3:
				if is_prime_pair(prime_pair[1], prime2):
					if is_prime_pair(prime_pair[2], prime2):
						prime_pair.append(prime2)
			elif len(prime_pair) == 4:
				if is_prime_pair(prime_pair[1], prime2):
					if is_prime_pair(prime_pair[2], prime2):
						if is_prime_pair(prime_pair[3], prime2):
							prime_pair.append(prime2)		
	if len(prime_pair) == 5:
		print(prime_pair)
		prime_pair.sort()
		prime_pair_list.append(prime_pair)

total_list = []
for pair_list in prime_pair_list:
	total = 0
	for prime in pair_list:
		total += prime
	total_list.append(total)

print(min(total_list))

