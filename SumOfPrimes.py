size = 2000000

s = set(range(2, size))

for i in range(2, len(s)):
    for j in range(i * 2, size, i):
        s.discard(j)
print(sum(filter(None, s)))
