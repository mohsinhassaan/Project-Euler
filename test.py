import timeit

a = """\
size = 20000

s = set(range(2, size))

for i in range(2, len(s)):
    for j in range(i * 2, size, i):
        s.discard(j)

"""

b = """
size = 20000

s = list(range(size))

for i in range(2, len(s) - 1):
    for j in range(i * 2, len(s) - 1, i):
        s.pop(j)
        s.insert(j, 0)
"""

print(
    f"set: {timeit.timeit(a, number = 1000)} usecs per loop\nlist: {timeit.timeit(b, number = 1000)} usecs per loop"
)
