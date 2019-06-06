from math import log


cache = set()


def load_primes(f):
    pset = set()
    try:
        with open(f, "r") as file:
            for line in file:
                pset.add(int(line.rstrip(",\n")))
    except Exception:
        with open(f, "w"):
            pass
        pset = load_primes(f)

    return pset


def primes(upper_bound, old=cache, only_new=False):
    """Returns set of primes less than n"""
    lower_bound = 2
    if type(old) == set:
        prime_set = new_primes(upper_bound, old, lower_bound)
        if not only_new:
            prime_set.update(old)
            old = prime_set
    elif old == set():
        prime_set = set(x for x in range(lower_bound, upper_bound))
        for i in range(lower_bound, upper_bound):
            prime_set = remove_multiples(i, prime_set, upper_bound)
    else:
        raise TypeError('old must be of type "set"')

    return prime_set


def new_primes(upper_bound, old, lower_bound):
    lower_bound = get_lower_bound(lower_bound, old)
    if lower_bound > upper_bound:
        prime_set = get_primes_below_upperb(old, upper_bound)
    else:
        prime_set = get_primes(lower_bound, upper_bound, old)
    return prime_set


def get_lower_bound(curr, Set):
    lower_bound = curr

    for n in Set:
        if n > curr:
            lower_bound = n

    return lower_bound


def remove_multiples(n, Set, limit):
    for i in range(n ** 2, limit, n):
        Set.discard(i)

    return Set


def get_primes_below_upperb(old, upper_bound):
    prime_set = set()
    for prime in old:
        if prime < upper_bound:
            prime_set.add(prime)

    return prime_set


def get_primes(lower_bound, upper_bound, old):
    prime_set = set(x for x in range(lower_bound, upper_bound))
    for prime in old:
        prime_set = remove_multiples(prime, prime_set, upper_bound)

    for i in range(lower_bound, upper_bound):
        if i ** 2 > upper_bound:
            break
        if i in prime_set:
            prime_set = remove_multiples(i, prime_set, upper_bound)

    return prime_set


def nth_prime(n):
    """Returns the nth prime"""

    upper_bound = 0
    if n >= 7022:
        upper_bound = int(n * log(n) + n * (log(log(n)) - 0.9385))
    elif n >= 6:
        upper_bound = int(n * log(n) + n * log(log(n)))
    else:
        upper_bound = 14
    prime_set = list(primes(upper_bound))
    return prime_set[n - 1]


def prime_factors(n):
    """Returns a list of the prime factors of n\n
        Only returns each factor once"""

    prime_set = primes(n)
    factors = []
    for prime in prime_set:
        if n % prime == 0:
            factors.append(prime)
    return factors


def is_prime(n):
    """Returns a boolean based on whether n is prime"""

    prime_set = primes(n + 1)
    return n in prime_set


if __name__ == "__main__":
    print(primes(100))

