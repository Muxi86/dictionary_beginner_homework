def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    count = 0
    for i in data:
        for j in i.values():
            if j == job:
                count += 1
    return count

data = [{
    'name': 'John',
    'job': 'Developer'
    },
    {'name': 'Mary',
     'job': 'Developer'
     }]

print(count_jobs(data,'Developer'))