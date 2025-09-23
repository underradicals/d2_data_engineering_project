def iterate_over(data: list):
    """Generator that yields items from a list one by one."""
    return [x * 10 for x in data]
