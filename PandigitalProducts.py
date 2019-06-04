def is_pandigital(number: str):
    for i in range(1, 10):
        if "0" in number or number.count(str(i)) != 1:
            return False
    return True


products = set()

for multiplicand in range(1, 10000):
    for multiplier in range(1, 1000):
        product = multiplicand * multiplier
        if is_pandigital(str(multiplicand) + str(multiplier) + str(product)):
            products.add(product)


print(sum(products))
