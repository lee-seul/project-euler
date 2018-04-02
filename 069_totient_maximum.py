# coding: utf-8
# 069_totient_maximum.py


# 수학&코딩 블로그 참조....

from lib.primes import is_prime


primes_list = [i for i in range(2, 101) if is_prime(i)]


n = 1
for x in range(len(primes_list)):
	n *= primes_list[x]
	if n > 1000000:
		break
	print(n)



