"""def divisors(num):
    n = 1
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            n += 1
    return n"""


def divisors(n):
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i * i <= nn:
        while nn % i == 0:
            factors[i] = factors.get(i, 0) + 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = factors.get(nn, 0) + 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k + 1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    # in python3, `yield from generate(0)` would also work
    for factor in generate(0):
        yield factor


def nth_triangle(n):
    ans = 0
    for i in range(n + 1):
        ans += i
    return ans


d = 0
num = 1
n = 1
while d <= 500:
    num = nth_triangle(n)
    d = 0
    for divisor in divisors(num):
        d += 1
    print(f"num: {num}, divisors: {d}")
    n += 1

print(num)
