def divide(dividend: int, divisor: int, size: int = 10000):
    quotient = ""
    while dividend != 0 and len(quotient) < size:
        try:
            decimal_found = True if quotient.index(".") >= 0 else False
        except ValueError:
            decimal_found = False

        if decimal_found:
            dividend *= 10

        if dividend < divisor and not decimal_found:
            quotient += "."
        else:
            current = 0
            while dividend >= divisor:
                dividend -= divisor
                current += 1
            quotient += str(current)

    if quotient[0] == ".":
        quotient = "0" + quotient

    return quotient


def get_reciprocal_cycle_length(dividend: int, divisor: int):
    quotient = divide(dividend, divisor)

    try:
        quotient.index(".")
        is_integer = False
    except ValueError:
        is_integer = True

    if is_integer:
        return 0
    else:
        fractional_part = quotient.split(".")[1]
        total_length = 0
        length = 0
        for index, digit in enumerate(fractional_part):
            current_index = 0
            next_index = index
            incrementable = True
            break_from_outer = False
            for i in range(fractional_part.count(digit)):

                current_index = next_index

                if current_index > len(fractional_part) // 2:
                    break

                try:
                    next_index = (
                        fractional_part[current_index + 1 :].index(digit)
                        + current_index
                        + 1
                    )
                except ValueError:
                    if incrementable:
                        total_length += 1
                        incrementable = False
                    continue

                length = next_index - index

                if length == 1:
                    continue

                if (
                    fractional_part[index:next_index]
                    == fractional_part[next_index : next_index + length]
                ):
                    break_from_outer = True
                    break

            if break_from_outer:
                break

        total_length += length

        return total_length


highest = 0
highest_num = 0

for i in range(2, 1000):
    current = get_reciprocal_cycle_length(1, i)
    if current > highest:
        highest = current
        highest_num = i

print(highest_num)
