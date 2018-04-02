# coding: utf-8
# 050_consecutive_prime_sum.py

from lib.primes import is_prime

primes = []

for i in range(2, 1000000):
	if is_prime(i):
		primes.append(i)

records = {}

n = 0
p = 1

while(n+p < len(primes)):
#	print(n+p)
	total = 0
	length = 0
	key_list = list(records.keys())
	for i in range(p):
		total += primes[n+i]
		length +=1
	if total < 1000000:
		p += 1
		if is_prime(total):
			if length in key_list:
				if records[length] < total:
					records[length] = total
			else:
				records[length] = total

	else:
		n+= 1
		p = 1

key_list = list(records.keys())
key_list.sort()
key_list.reverse()

print(key_list)

for i in key_list:
	if is_prime(records[i]):
		print(i,records[i])
		break




