# coding: utf-8
# 019_counting_sundays.py

year = 1901
n =[6, 5, 4, 3, 2, 1, 0]
x = 0
l = []
l_yearly = []
while(year!=2001):
	x = x % 7
	if year % 4 == 0:
		for i in range(1 ,367):
			if i % 7 == n[x]:
				l.append(i)
		x += 1
				
	else: 
		for i in range(1, 366):
			if i % 7 == n[x]:
				l.append(i)
		x += 1
	year += 1
	l_yearly.append(l)
	l = []

nomal_mon = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
spec_mon = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]

result = 0
for k in range(len(l_yearly)):
	if k % 3 == 0:
		for z in range(len(l_yearly[k])):
			if l_yearly[k][z] in spec_mon:
				result += 1
	
	else:
		for z in range(len(l_yearly[k])):
			if l_yearly[k][z] in nomal_mon:
				result += 1
	
print(result)





		
	

