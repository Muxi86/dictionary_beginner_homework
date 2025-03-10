def sum_age_values(data:list) -> int:
    """
    Return the sum of all age values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all age values in the dictionary
    """
    age = 0
    for i in data:
        age += i['age']
    return age
data = [{
    'name': 'John',
    'age': 27
    },
    {
    'name': 'Mary',
    'age': 42}]
print(sum_age_values(data))