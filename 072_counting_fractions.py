# coding: utf-8
# 072_counting_fractions.py


def count_fraction(n):
	num = [i for i in range(n+1)]
	for i in range(2, n+1):
		if num[i] == i:
			for k in range(i, n+1, i):
				num[k] -= num[k] // i
	return sum(num) -1

print(count_fraction(1000000))






