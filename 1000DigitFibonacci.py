current = 1
last = 0
index = 1

while current < 10 ** 999:
    current, last = current + last, current
    index += 1

print(index)
