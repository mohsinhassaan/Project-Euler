def collatz(start):
    current = start
    length = 1
    while current != 1:
        length += 1
        if not current & 1:
            current //= 2
        else:
            current = current * 3 + 1
    return length


longest = 0
n = 0

print(f"this: {collatz(837799)}, other: {collatz(766008)}")

# for i in range(1, 1_000_000):
#     length = collatz(i)
#     if length > longest:
#         longest = length
#         n = i

# print(n)
