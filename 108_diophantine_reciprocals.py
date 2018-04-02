# coding: utf-8
# 108_diophantine_reciprocals.py

n =1

count = 0

while(count<1000):
	count = 0
	print(n)
	for x in range(1, n):
		for y in range(1, n):
			if 1/x + 1/y < n/1:
				break
			elif 1/x + 1/y == 1/n:
				count+=1
	n+=1

print(n)
