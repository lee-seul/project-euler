# coding: utf-8
# 092_square_digit_chains.py

def digit_square_sum(num):
	return sum([int(i)**2 for i in str(num)])


def check_89(num):
    count = 0
    for i in range(1, num):
        print(i)
        result = digit_square_sum(i)
        while(True):
            if result == 89:
                count +=1
                break
            elif result == 1:
                break
            else:
                result = digit_square_sum(result)
    return print(count)

check_89(10000000)


