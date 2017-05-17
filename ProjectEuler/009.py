a = -1
b = -1
c = -1

done = False
for i in range(1,1001):
	for j in range(1,1001):
		for k in range(1,1001):
			if i + j + k != 1000:
				continue
			if (i * i) + (j * j) == (k * k):
				a = i
				b = j
				c = k
				done = True
				break

		if done:
			break
	if done:
		break

print(str(a * b * c))