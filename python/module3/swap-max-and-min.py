def swap_max_and_min(list: list):
    min_value = None
    max_value = None
    min_index = None
    max_index = None
    for value in list:
        if not min_value or not max_value:
            min_value = value
            min_index = list.index(value)
            max_value = value
            max_index = list.index(value)
        elif value == min_value or value == max_value:
            raise ValueError("Duplicate numbers.")
        elif not isinstance(value, (int, float)):
            raise TypeError("Not int or float.")
        elif value > max_value:
            max_value = value
            max_index = list.index(value)
        elif value < min_value:
            min_value = value
            min_index = list.index(value)
    list[min_index] = max_value
    list[max_index] = min_value
    return list