def multiply_in_range(start: int, stop: int):
    result = []
    for number in range(start, stop + 1):
        print(number)
        if number % 7 == 0 and number % 5 != 0:
            result.append(number)
    return result
