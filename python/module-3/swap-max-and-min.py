def swap_max_and_min(list: list):
    min_value = None
    max_value = None
    for value in list:
        if not min_value or not max_value:
            min_value = value
            max_value = value
        elif value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value
    list[list.index(min_value)] = max_value
    list[list.index(max_value)] = min_value
    print(list[list.index(min_value)])
    return list, min_value, max_value

print(swap_max_and_min([1,2,3,4,5,6,7]))