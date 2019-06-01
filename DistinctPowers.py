MIN = 2
MAX = 100

numbers = {a ** b for b in range(MIN, MAX + 1) for a in range(MIN, MAX + 1)}

print(len(numbers))
