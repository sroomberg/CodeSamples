l = [x for x in range(1,101)]
squares = [e * e for e in l]
sum_of_squares = sum(squares)
square_of_sum = sum(l) * sum(l)
print(str(square_of_sum - sum_of_squares))