'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def is_prime(n):
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif n % 2 == 0 or n % 3 == 0:
		return False

	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6

	return True

which_prime = 0
cur_num = 1
while which_prime < 10001:
	cur_num += 1
	if is_prime(cur_num):
		which_prime += 1

print(str(cur_num))