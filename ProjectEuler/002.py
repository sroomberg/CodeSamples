
i, one, two, fib_sum = 0, 0, 1, 0

while True:
	if i <= 1:
		next_num = i
	else:
		next_num = one + two
		one = two
		two = next_num
		if two < 4000000:
			if two % 2 == 0:
				fib_sum += two
		else:
			break
	i += 1

print(str(fib_sum))