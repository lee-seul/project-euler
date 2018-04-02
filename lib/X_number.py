# coding: utf-8
# X_number.py

from math import sqrt

def is_triangle(num):
	n = abs(num)
	p = (sqrt(1+n*8)-1)/2
	return p == int(p)

def num_3(num):
	return int((num*(num+1))/2)


def num_4(num):
	return num**2


def is_pentagon(num):
	n = abs(num)
	p = (sqrt(1+24*n)+1)/6
	return p == int(p)


def num_5(num):
	return int(num*(3*num-1)/2)

def is_hexagon(num):
	n = abs(num)
	p = (sqrt(1+8*n)+1)/4
	return p == int(p)


def num_6(num):
	return num*(2*num-1)


def num_7(num):
	return int((num*(5*num-3))/2)

def num_8(num):
	return num*(3*num-2)

