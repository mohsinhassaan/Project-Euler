grid = []
with open("grid.txt") as f:
    for line in f:
        grid.append(line.rstrip("\n").split())

largest = 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        product = 0

        # Up
        if x > 2:
            prod = (
                int(grid[x][y])
                * int(grid[x - 1][y])
                * int(grid[x - 2][y])
                * int(grid[x - 3][y])
            )
            product = prod if prod > product else product

        # Down
        if x < len(grid) - 3:
            prod = (
                int(grid[x][y])
                * int(grid[x + 1][y])
                * int(grid[x + 2][y])
                * int(grid[x + 3][y])
            )
            product = prod if prod > product else product

        # Left
        if y > 2:
            prod = (
                int(grid[x][y])
                * int(grid[x][y - 1])
                * int(grid[x][y - 2])
                * int(grid[x][y - 3])
            )
            product = prod if prod > product else product

        # Right
        if y < len(grid[x]) - 3:
            prod = (
                int(grid[x][y])
                * int(grid[x][y + 1])
                * int(grid[x][y + 2])
                * int(grid[x][y + 3])
            )
            product = prod if prod > product else product

        # Top-Left
        if x > 2 and y > 2:
            prod = (
                int(grid[x][y])
                * int(grid[x - 1][y - 1])
                * int(grid[x - 2][y - 2])
                * int(grid[x - 3][y - 3])
            )

            product = prod if prod > product else product

        # Top-Right
        if x > 2 and y < len(grid[x]) - 3:
            prod = (
                int(grid[x][y])
                * int(grid[x - 1][y + 1])
                * int(grid[x - 2][y + 2])
                * int(grid[x - 3][y + 3])
            )
            product = prod if prod > product else product

        # Bottom-Left
        if x < len(grid) - 3 and y > 2:
            prod = (
                int(grid[x][y])
                * int(grid[x + 1][y - 1])
                * int(grid[x + 2][y - 2])
                * int(grid[x + 3][y - 3])
            )
            product = prod if prod > product else product

        # Bottom-Right
        if x < len(grid) - 3 and y < len(grid[x]) - 3:
            prod = (
                int(grid[x][y])
                * int(grid[x + 1][y + 1])
                * int(grid[x + 2][y + 2])
                * int(grid[x + 3][y + 3])
            )
            product = prod if prod > product else product

        if product > largest:
            largest = product

print(largest)
