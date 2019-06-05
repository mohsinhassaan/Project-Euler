from math import factorial


def num_to_digits(num: int):
    digits = []
    while num != 0:
        digits.append(num % 10)
        num //= 10
    return digits


upper_bound = factorial(9) * 8
digit_factorials = []

for i in range(3, upper_bound):
    digits = num_to_digits(i)
    total = 0
    for digit in digits:
        if total >= i:
            break
        total += factorial(digit)
    else:
        if total == i:
            digit_factorials.append(i)

print(sum(digit_factorials))
