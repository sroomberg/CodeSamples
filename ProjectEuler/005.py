'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

n = 2520
div = [x for x in range(2,21)]
loop_counter = 0

while True:
	for i in div:
		loop_counter += 1
		if n % i != 0:
			break
	if loop_counter == len(div):
		print(str(n))
		break
	else:
		loop_counter = 0
		n += 20