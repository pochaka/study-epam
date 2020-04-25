def dict_swap(dictionary):
    try:
        result = {value: key for key, value in dictionary.items()}
    except TypeError:
        raise TypeError("Some wrong data in dictionary.")
    return result