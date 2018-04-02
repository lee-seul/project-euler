# coding: utf-8
# 024_lexicographic.py

string = '0123456789'

def perm(st):
	leng = len(st)
	if leng == 1:
		return [st]
	else:
		result = []
		for i in range(len(st)):
			r = st[:i]+st[i+1:]
			for j in perm(r):
				result.append(st[i:i+1]+j)
		return result

#l = list(perm(string).sort())

print(perm(string)[999999])
#print(l[999999])

