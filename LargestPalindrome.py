pal = 0


def isPalindrome(num):
    num = str(num)
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            return False
    return True


for i in range(999, 100, -1):
    if pal > i * 999:
        break
    for j in range(i, 100, -1):
        num = i * j
        print(f"i: {i}, j: {j}, num: {num}, palindrome: {isPalindrome(num)}")
        if isPalindrome(num) and num > pal:
            pal = num


print(f"palindrome: {pal}")
