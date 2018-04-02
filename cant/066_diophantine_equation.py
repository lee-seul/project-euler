# coding: utf-8
# 066_diophantine_equation.py

from math import sqrt


def is_diophantine(D, y):
	x = D*y**2+1
	if int(sqrt(x)) == sqrt(x):
		return True
	else:
		return False


def bigest_diophantine(num):
	D_list = [i for i in range(2, num+1) if int(sqrt(i))!=sqrt(i)]
	y = 1
	while(len(D_list)!=1):
		print(y, len(D_list))	
		l = []
		for D in D_list:
			if is_diophantine(D, y):
				l.append(D)
		for n in l:
			D_list.remove(n)
		y += 1
	return D_list[0]


print(bigest_diophantine(1000))



