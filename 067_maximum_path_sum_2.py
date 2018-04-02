# coding: utf-8
# 067_maximum_path_sum_2.py

f = open('067_maximum_path_sum_2.txt')

triangle_num = f.read().split('\n')
for x in range(len(triangle_num)):
	triangle_num[x] = triangle_num[x].split(' ')
	if x == len(triangle_num)-1:
		continue
	else:
		for y in range(len(triangle_num[x])):
			triangle_num[x][y] = int(triangle_num[x][y])

del triangle_num[-1]

triangle_num.reverse()



for x in range(len(triangle_num)):
	for y in range(len(triangle_num[x])-1):
		triangle_num[x+1][y] += max(triangle_num[x][y], triangle_num[x][y+1])

print(triangle_num[-1][-1])


	



