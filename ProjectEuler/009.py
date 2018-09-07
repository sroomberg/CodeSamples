'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

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