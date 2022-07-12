def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    i = 1
    num = {}
    while i < len(key):
        for e in value:
            num[i] = e
        
        
    return num
print(create_dictionary())