def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        x = n - 1
        while x > 1:
            n *= x
            x -= 1
    return n


n = str(factorial(100))
total = 0

for digit in n:
    total += int(digit)

print(total)
