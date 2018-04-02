# coding: utf-8
# 059_xor_decrytion.py

from itertools import permutations as pm


f = open('059_cipher1.txt')

data = f.read().split(',')
data[-1] = data[-1][:2]

alphabet = []


for num in range(len(data)):
	data[num] = int(data[num])


for i in range(97, 123): # ord('a') == 97, ord('z') == 122
	alphabet.append(i)
	
length = len(data)

keys_list = list(pm(alphabet, 3))

answer = []
count = 0
#key = []
for keys in keys_list:
	keys = list(keys)
	decrytion = []
	n = 0
	for x in data:
		decrytion.append(x^keys[n])
		n+=1
		if n == 3:
			n = 0
	if count < decrytion.count(32):
		count = decrytion.count(32)
		answer = decrytion
#		key = keys

result = 0
for num in answer:
	result += num
print(result)
