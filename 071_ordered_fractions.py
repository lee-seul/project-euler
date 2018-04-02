# coding: utf-8
# 071_ordered_fractions.py

a, c = 2, 5
b, d = 3, 7

while(c+d <= 1000000):
	a += b
	c += d

print(a)
