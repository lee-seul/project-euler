# coding: utf-8
# 053_combinatoric_selections.py

from lib.permutation_combinations import combination


result = 0

for n in range(1, 101):
	for r in range(1, n+1):
		if combination(n, r) > 1000000:
			result += 1

print(result)



