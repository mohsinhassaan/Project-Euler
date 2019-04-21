size = 21
grid = [["x" for i in range(size)] for j in range(size)]


for i in range(len(grid)):
    grid[0].pop(i)
    grid[0].insert(i, 1)

    grid[i].pop(0)
    grid[i].insert(0, 1)

for i in range(1, len(grid)):
    for j in range(1, len(grid[i])):
        grid[i].pop(j)
        grid[i].insert(j, grid[i - 1][j] + grid[i][j - 1])

print(grid[len(grid) - 1][len(grid[0]) - 1])
