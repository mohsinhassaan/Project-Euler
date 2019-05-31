def get_next_direction(current_direction):
    return current_direction + 1 if current_direction < 3 else 0


def new_position(current_position, direction):
    new_position = current_position
    if direction == 0:
        new_position["x"] += 1
    elif direction == 1:
        new_position["y"] += 1
    elif direction == 2:
        new_position["x"] -= 1
    elif direction == 3:
        new_position["y"] -= 1

    return new_position


def generate_spiral(size: int):
    spiral = [[0 for j in range(size)] for i in range(size)]

    steps_left = [1, 1, 2, 2]
    current_steps_left = steps_left.copy()

    direction = 0

    current_position = {"x": size // 2, "y": size // 2}

    spiral[current_position["y"]][current_position["x"]] = 1

    for i in range(2, size ** 2 + 1):
        if current_steps_left[direction] == 0:
            steps_left[direction] += 2
            current_steps_left[direction] = steps_left[direction]
            direction = get_next_direction(direction)

        current_steps_left[direction] -= 1

        current_position = new_position(current_position, direction)
        spiral[current_position["y"]][current_position["x"]] = i

    return spiral


def sum_diagonals(square):
    total = square[len(square) // 2][len(square) // 2]
    for i in range(len(square) // 2):
        total += square[i][i]
        total += square[i][len(square) - i - 1]
        total += square[len(square) - i - 1][i]
        total += square[len(square) - i - 1][len(square) - i - 1]
    return total


if __name__ == "__main__":
    SIZE = 1001
    spiral = generate_spiral(SIZE)
    sum_of_diagonals = sum_diagonals(spiral)
    print(sum_of_diagonals)
