'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

i, j, cur_max = 999, 999, 0

while True:
	p = i * j
	p_str = str(p)
	if p_str == p_str[::-1]:
		if p > cur_max:
			cur_max = p
	if j > 99:
		j -= 1
	else:
		j = 999
		i -= 1
		if i == 99:
			break

print(str(cur_max))