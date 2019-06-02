def can_be_written_as_fifth_power(num):
    digits = [int(digit) for digit in str(num)]
    total = 0
    for digit in digits:
        total += digit ** 5
    return True if total == num else False


MIN = 2 * (2 ** 5)
MAX = 5 * (9 ** 5) + 1

total = 0

for i in range(MIN, MAX):
    if can_be_written_as_fifth_power(i):
        total += i

print(total)
