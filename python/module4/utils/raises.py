def raises(error):
    def func_deco(func):
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except Exception:
                raise error
            return res
        return wrapper
    return func_deco
