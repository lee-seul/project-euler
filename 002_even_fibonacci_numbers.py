# coding: utf-8
# 002_even_fibonacci_numbers.py

l = [1, 1]
total = 0 

while(l[-1] < 4000000):
	l.append(l[-1]+l[-2])
	if l[-1] % 2 == 0:
		total += l[-1]
	
print(total)



