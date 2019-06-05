from primes import primes

prime_set = primes(1_000_000)


def is_prime(num: int):
    return num in prime_set


def rotate(num: int):
    rotations = set()
    last_rotation = str(num)

    for i in range(len(last_rotation)):
        last_rotation = (
            last_rotation[len(last_rotation) - 1]
            + last_rotation[: len(last_rotation) - 1]
        )
        rotations.add(int(last_rotation))

    return rotations


to_skip = set()

count = 0

for i in range(1_000_000):
    if not i in to_skip:
        rotations = rotate(i)
        for rotation in rotations:
            if not is_prime(rotation):
                break
        else:
            count += len(rotations)
        to_skip.update(rotations)


print(count)
