# coding: utf-8
# 042_coded_triangle_numbers.py

from lib.X_number import is_triangle


data = open('042_coded_triangle_numbers.txt').read().replace('"', '').split(',')


dic = {'A':1, 'B':2,'C':3, 'D': 4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
	   'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17,
	   'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24,'Y':25,
	   'Z':26}

keys_list = list(dic.keys())


count = 0

for word in data:
	total = 0
	for x in word:
		if x in keys_list:
			total += dic[x]
	if is_triangle(total):
		count+= 1
	
print(count)

