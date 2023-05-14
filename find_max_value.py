def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    return max(data.values())

data = {'a': -2.5, 'b': 3.2, "c" : 7.1}
print(find_max_value(data))