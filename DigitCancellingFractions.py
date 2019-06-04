def gcd(a, b):
    if a == 0:
        return b

    if b == 0:
        return a

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def to_lowest_terms(num, den):
    hcf = gcd(num, den)
    lowest_terms = [num // hcf, den // hcf]
    return lowest_terms


def is_digit_cancelling(num, den):
    lowest_terms = to_lowest_terms(num, den)
    numerator = [num // 10, num % 10]
    denominator = [den // 10, den % 10]

    for i in range(2):
        for j in range(2):
            if numerator[i] == denominator[j]:
                numerator.pop(i)
                denominator.pop(j)
                break
        else:
            continue
        break
    else:
        return False

    if to_lowest_terms(numerator[0], denominator[0]) == lowest_terms:
        return True
    else:
        return False


found = 0
mult_num = 1
mult_den = 1


for denominator in range(10, 100):
    if denominator % 10 == 0:
        continue
    for numerator in range(10, denominator + 1):
        if numerator == denominator or (numerator % 10 == 0 and denominator % 10 == 0):
            continue
        if is_digit_cancelling(numerator, denominator):
            mult_num *= numerator
            mult_den *= denominator
            found += 1

mult_den = to_lowest_terms(mult_num, mult_den)[1]

print(mult_den)
