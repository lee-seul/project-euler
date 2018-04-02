# coding: utf-8
# 017_number_letter_counts.py

from math import floor

def num_to_letter(num):
	total = 0
	num_str = str(num)
	letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	letters2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	if num > 0 and num < 20:
		return letters[num-1]
	elif num >= 20 and num < 100:
		if num % 10 ==0:
			return letters2[int(num/10)-2]
		else:
			return letters2[int(num/10)-2] + '-' + letters[(num%10)-1]
	elif num >= 100 and num < 1000:
		if num % 100 == 0:
			return letters[int((num/100)-1)] + ' hundred'
		else:
			num_str = num - (int(num_str[0]) * 100)
			if num_str > 0 and num_str < 20:
				return letters[int((num/100)-1)] + ' hundred and ' + letters[num_str-1] 
			elif num_str >= 20 and num_str < 100:
				if num_str % 10 == 0:
					return letters[int((num/100)-1)] + ' hundred and ' + letters2[int(num_str/10)-2] 
				else:
					return letters[int((num/100)-1)] + ' hundred and ' + letters2[int(num_str/10) -2] + '-' + letters[(num_str%10)-1]
	elif num == 1000:
		return 'one thousand'


result = 0
for i in range(1, 1001):
	result += len(str(num_to_letter(i)).replace(' ', '').replace('-', ''))

print(result)



