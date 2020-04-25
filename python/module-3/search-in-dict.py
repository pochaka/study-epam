def extra(var1, var2):
    result = []
    if isinstance(var1, dict) and isinstance(var2, (list, set)):
        dictionary = var1
        setlist = var2
    elif isinstance(var1, (list, set)) and isinstance(var2, dict):
        dictionary = var2
        setlist = var1
    else:
        raise TypeError("Wrong arguments.")
    for key, value in dictionary.items():
        for item in setlist:
            if item == key or item == value:
                result.append(item)
    return result