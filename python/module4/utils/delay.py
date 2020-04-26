def delay(func):
    def wrapper(*args, **kwargs):
        from time import sleep
        sleep(3)
        res = func(*args, **kwargs)
        return res
    return wrapper