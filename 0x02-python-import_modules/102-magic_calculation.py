def magic_calculation(a, b):
    result = 0

    if a < b:
        result = add(a, b)
    else:
        result = sub(a, b)

        for i in range(4, 6):
            result = add(result, i)

    return result
