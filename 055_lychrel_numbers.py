# coding: utf-8
# 055_lychrel_numbers.py


def is_palindrome(num):
	num =list(str(num))
	j = -1
	for i in range(0, len(num)):
		if num[i] != num[j-i]:
			return False
	return True


def num_reverse_plus(num):
	reverse_l = list(str(num))
	reverse_l.reverse()
	reverse_num = ''
	for l in reverse_l:
		reverse_num += l
	reverse_num = int(reverse_num)
	return num+reverse_num
		
count = 0

for i in range(1, 10001):
	n = 0
	num = num_reverse_plus(i)
	while(True):
		if n < 50:
			n += 1
			if is_palindrome(num):
#				print(num)
				break
			else:
				num = num_reverse_plus(num)
		elif n ==50:
			count += 1
			break

print(count)


