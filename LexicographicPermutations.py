from itertools import permutations

permutation_lst = list(permutations(range(10)))

num = 0

for digit in permutation_lst[999999]:
    num *= 10
    num += digit

print(num)
