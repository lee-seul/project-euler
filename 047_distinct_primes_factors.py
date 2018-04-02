# coding: utf-8
# 047_distinct_primes_factors.py

from lib.primes import find_primes_factor as ff


def check_duplication(l):
	i = 0
	while(i<len(l)-1):
		if l[i] % l[i+1] == 0:
			l.remove(l[i+1])
			l[i] *= l[i]
		else:
			i += 1
	return l

def comparison_list(list1, list2, list3, list4):
	l = []
	l = list1 + list2 + list3 + list4
	l.sort()
	l_set = list(set(l))
	l_set.sort()
	if l == l_set:
		return True
	else:
		return False
	
n = 2
while(True):
	p1 = check_duplication(ff(n))
	p2 = check_duplication(ff(n+1))
	p3 = check_duplication(ff(n+2))
	p4 = check_duplication(ff(n+3))
	if len(p1) == 4 and len(p2) == 4 and len(p3) == 4 and len(p4) == 4:
		if comparison_list(p1, p2, p3, p4):
			print(n)
			break
		else:
			n+= 1
	else:
		n += 1


