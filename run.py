def increment(number):
    """
    function that returns incremented number

    arguments:
        number - a whole number to incremet
    """
    if isinstance(number, int):
        return number + 1
    else:
        return 'you can only increment whole numbers!'
