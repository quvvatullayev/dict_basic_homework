from platform import java_ver


def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    i = 0
    javob = {}
    while i < len(cities):
        javob[i] = cities[i]
        i += 1
    return javob

print(cities_dict(["Bukhara", "Khiva", "Namangan", "Samarkand", "Tashkent"]))