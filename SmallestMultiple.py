multiple = 0
num = 0
nums = [x for x in range(1, 21)]

while multiple == 0:
    num += 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
    isMultiple = False
    for n in nums:
        if num % n != 0:
            isMultiple = False
            break
        else:
            isMultiple = True
    if isMultiple:
        multiple = num

print(multiple)
