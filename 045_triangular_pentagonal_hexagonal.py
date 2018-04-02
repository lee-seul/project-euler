# coding: utf-8
# 045_triangular_pentagonal_hexagonal.py

from lib.X_number import num_3, is_pentagon, is_hexagon

n = 286

while(True):
	tri_num = num_3(n)
	if is_pentagon(tri_num) and is_hexagon(tri_num):
		print(tri_num)
		break
	n += 1



