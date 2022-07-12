from operator import index


def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    name = people.keys()
    name = list(name)
    young = people.values()
    max_young = max(young)
    index_name = list(young).index(max_young)
 
    return name[index_name]
print(oldest({"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}))