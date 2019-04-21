nums = []

with open("number.txt") as f:
    for line in f:
        nums.append(int(line.rstrip("\n")))

total = 0

for num in nums:
    total += num

print(str(total)[:10])
