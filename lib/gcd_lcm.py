# coding: utf-8
# gcd_lcm.py


# 유클리드 호제법을 이용한 최소 공배수와 최대 공약수 

# 최대 공약수 
def gcd(a, b):
	if a % b == 0:
		return b
	return gcd(b, a%b)

# 최소 공배수
def lcm(a, b):
	return int(a*b/gcd(a,b))


