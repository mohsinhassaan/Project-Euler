a = 1
b = 1
c = 0
Sum = 0

while a <= 4_000_000:
    Sum += a if a % 2 == 0 else 0
    a = b + c
    c = b
    b = a

print(Sum)
