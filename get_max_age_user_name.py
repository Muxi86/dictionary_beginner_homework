def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    for i in data:
        for j in i.values():
            print(j)
    return 
data = [{
    'name': 'John',
    'age': 32
    }, 
    {'name': 'Mary',
     'age': 18
     }, 
    {'name': 'Ann',
     'age': 20
     },
    {'name': 'Ban',
     'age': 29
     }]
print(get_max_age_user_name(data))