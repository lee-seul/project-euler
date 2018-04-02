# coding: utf-8
# 028_spiral_diagonals.py


num = 1
plus = 2
result = 0
i = 0
while(num<=1001**2):
	result += num
	num += plus
	i+=1
	if i % 4 == 0:
		plus += 2

print(result)
	


