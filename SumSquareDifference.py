sum_of_squares = 0
square_of_sums = 0

for i in range(1, 101):
    sum_of_squares += i ** 2
    square_of_sums += i

square_of_sums **= 2

difference = square_of_sums - sum_of_squares

print(difference)
