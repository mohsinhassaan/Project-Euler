abundants = []
abundant_sums = set()
for i in range(12, 28123):
    add = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            add += j
        if add > i:
            abundants.append(i)
            break

total_num = list(range(1, 28124))

for k in range(len(abundants)):
    for l in range(k, len(abundants)):
        add = 0
        add = abundants[k] + abundants[l]
        if add <= 28123:
            abundant_sums.add(add)
print(sum(total_num) - sum(abundant_sums))

