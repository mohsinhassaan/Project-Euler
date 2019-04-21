def pds(n, power):
    num = n ** power
    ans = 0
    for digit in str(num):
        ans += int(digit)
    return ans


print(pds(2, 1000))
