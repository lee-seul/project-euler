# coding: utf-8
# 026_reciprocal_cycles.py

def prime_factor(num):
	l = []
	x = 2
	while(num!=1):
		if num % x == 0:
			l.append(x)
			num = int(num/x)
		else:
			x+=1
	return l


def find_num(num):
	total = 1
	l = prime_factor(num)
	while(True):
		if 2 in l:
			l.remove(2)
		elif 5 in l:
			l.remove(5)
		else:
			break
	for x in l:
		total *= x
	return total


def find_cycle_length(num):
	total = find_num(num)
	n = 1
	while(True):
		if ((10**n)-1) % total == 0:
			return n
		else:
			n+=1

last_result = 0
mid = 0
first = 0
for i in range(2, 1001):
	mid = find_cycle_length(i)
	if mid > first:
		first = mid
		last_result = i
 

print(last_result)






