# coding: utf-8
# 081_two_ways.py

matrix = []
for line in open('081_matrix.txt').read().split('\n'):
	matrix.append(line.split(','))

del matrix[-1]

for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		matrix[i][j] = int(matrix[i][j])
x = 0
y = 0
result = 0

while(True):
	print(x, y, result)
	result += matrix[x][y]
	if x < 79 and y < 79:  
		if matrix[x+1][y] >= matrix[x][y+1]:
			y+=1
		elif matrix[x+1][y] < matrix[x][y+1]:
			x+=1	
	elif x == 79 and y != 79:
		y+=1
	elif y == 79 and x != 79:
		x+=1
	elif x == 79 and y == 79:
		break

result += matrix[79][79]

print(result)


