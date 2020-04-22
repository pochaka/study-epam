def lists_2_dict(list1, list2):
    try:
        dictionary = dict(zip(list1, list2))
    except TypeError:
        raise TypeError("Some wrong data in lists.")
    return dictionary