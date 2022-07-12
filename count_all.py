def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    i = 0
    son = 0
    harf = 0
    javob = { "LETTERS":  0, "DIGITS": 0 }
    while i < len(txt):
        if str(txt[i]).isdigit():
            son += 1
        elif str(txt[i]).isalpha():
            harf += 1

        i += 1
    javob["LETTERS"] = harf
    javob["DIGITS"] = son

    return javob
print(count_all("djhuer89"))