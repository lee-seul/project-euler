# coding: utf-8
# constant.py

# 상수 e 는 limit n->무한 (1+1/n)**n

def limit_e(num):
	return (1+1/num)**num


# 혹은 시그마(0->무한) 1/n!

def sigma_e(num):
	total = 0
	n = 1
	for i in range(1, num+1):
		n *= i
		total += 1/n
	return total+1

	
