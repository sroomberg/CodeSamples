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