def is_palindrome(string: str):
    return string == string[::-1]


total = 0

for i in range(1_000_000):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        total += i

print(total)
