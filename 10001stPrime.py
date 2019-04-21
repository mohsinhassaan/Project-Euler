def isPrime(num):
    if num == 1 or num == 0:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, num // 2, 2):
        if num != i and num % i == 0:
            return False
    return True


count = 0
num = 0

while count < 10001:
    num += 1
    if isPrime(num):
        count += 1

print(num)
