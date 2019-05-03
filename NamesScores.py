score = 0
word_score = 0
names = []

current_word = ""

with open("names.txt", "r") as file:
    names = sorted(file.read().replace('"', "").split(","))

print(names[:6])

for i, name in enumerate(names):
    for character in name:
        word_score += ord(character) - ord("A") + 1
    score += word_score * (i + 1)
    word_score = 0

print(score)
