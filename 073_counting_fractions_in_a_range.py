# coding: utf-8
# 073_counting_fractions_in_a_range.py

from lib.gcd_lcm import gcd


count = 0
for d in range(2, 12001):
	print(d)
	for n in range(1, d):
		if n/d > 1/3 and n/d < 1/2:
			if gcd(n, d) == 1:
				count += 1

print(count)




