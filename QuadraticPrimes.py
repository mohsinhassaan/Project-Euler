from primes import primes

prime_set = primes(3000000)


def formula_test(a: int, b: int):
    ans = 0
    n = -1
    while True:
        n += 1
        ans = n ** 2 + a * n + b
        if ans < 0 or ans not in prime_set:
            break
    return n


maximum = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        product = a * b
        current = formula_test(a, b)
        if current > maximum:
            maximum = current
            max_product = product

print(max_product)
