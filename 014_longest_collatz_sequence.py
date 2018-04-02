# coding: utf-8
# 014_longest_collatz_sequence.py

#def collatz(num, count):
#	count += 1
#	if num != 1:	
#		if num % 2 == 0:
#			collatz(num/2, count)
#		elif num % 2 == 1:
#			collatz((num*3)+1, count)
#	elif num == 1:
#		return count

def collatz(num):
	count = 0
	while(num!=1):
		count += 1
		if num % 2 ==0:
			num = num/2
		elif num % 2 == 1:
			num = (num*3)+1
	return count


result = 0
n = 0
cnt = 0

for i in range(100000, 1000001):
	cnt = collatz(i)
#	print(cnt)
	if cnt > result:
		result = cnt
		n = i

print(n)

			
