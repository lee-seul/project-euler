# coding: utf-8
# 039_integer_right_triangles.py

from math import sqrt

result = []

p = 1000
for a in range(1, 500):
	for b in range(1, 500):
		c = sqrt(a**2 + b**2)
		if c == int(c) and a+b+c <= p:
			result.append(a+b+c)
		
count = {}

for num in result:
	count[num] = result.count(num)


key_list = list(count.keys())

max_result = 0
max_p = 0
for key in key_list:
	if max_result < count[key]:
		max_result = count[key]
		max_p = key

print(int(max_p))


