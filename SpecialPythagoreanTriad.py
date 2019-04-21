from math import sqrt


class BreakIt(Exception):
    pass


# def isPythagoreanTriad(a, b, c):
#     if (
#         not float(a).is_integer()
#         or not float(b).is_integer()
#         or not float(c).is_integer()
#     ) and (a <= 0 or b <= 0 or c <= 0):
#         return False
#     if a ** 2 + b ** 2 == c ** 2:
#         return True
#     else:
#         return False

abc = 0

try:
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = sqrt(a ** 2 + b ** 2)
            # print(f"a: {a}, b: {b}, c: {c}")
            if c.is_integer() and a + b + c == 1000:
                abc = a * b * c
                raise BreakIt
except BreakIt:
    pass

print(abc)
