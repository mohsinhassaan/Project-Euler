def prime_factors(n):
    factors = []
    primes = [x for x in range(int(sqrt(n)))]

    num = n
    x = 2
    while num % 2 == 0:
        num //= 2
        factors.append(2)
    while num != 1:
        if num % x == 0:
            num //= x
            factors.append(x)
        x += 2
    return factors


def all_factors(primefacs):
    factors = primefacs
    for factor in primefacs:
        f


def d(n):
    


total = 0
for a in range(10000):
    for b in range(a):
        if d(a) == b and d(b) == a:
            print(a, b)
            total += a + b

print(total)
