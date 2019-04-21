temp = []

with open("triangle.txt") as file:
    for line in file:
        line = line.rstrip("\n")
        temp.append(line)

triangle = []

for i in range(len(temp)):
    x = temp[i].split()
    triangle.append([])
    for elem in x:
        triangle[i].append(int(elem))
x.clear()
temp.clear()

for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        x = triangle[i].pop(j)
        if triangle[i + 1][j] > triangle[i + 1][j + 1]:
            triangle[i].insert(j, x + triangle[i + 1][j])
        else:
            triangle[i].insert(j, x + triangle[i + 1][j + 1])
        print(triangle[i][j], end=" ")
    print()
