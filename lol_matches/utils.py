def safe_get(dict, *args):
    value = dict
    for arg in args:
        try:
            value = value.get(arg)
        except:
            return None
    return value
