# coding: utf-8
# 015_lattice_paths.py

def lattice_paths(x, y):
	result = 0
	x_multi = 1
	y_multi = 1
	n = 1
	if x > 1 and y > 1:
		for i in range(1, (x*2)+1):
			x_multi *= i
		for j in range(1, y+1):
			y_multi *= j
		for k in range(1, ((x*2)-y)+1):
			n *= k
		result = x_multi/(y_multi*n)
		return result
	else:
		print("END")

print(lattice_paths(20, 20))


