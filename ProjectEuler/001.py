
ret = 0
for i in range(0,1000):
	# if i % 3 == 0 and i % 5 == 0:
	# 	continue
	if i % 3 == 0:
		ret += i
	elif i % 5 == 0:
		ret += i

print(str(ret))