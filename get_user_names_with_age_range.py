def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    names = []
    for i in data:
        if i['age']==min_age or i['age']==max_age:
            names.append(i['name'])
    return names
data = [{'name': 'Anny', 'age': 20}, 
        {'name': 'Ann', 'age': 30}, 
        {'name': 'John', 'age': 11}, 
        {'name': 'Mary', 'age': 27}]
print(get_user_names_with_age_range(data,11,30))