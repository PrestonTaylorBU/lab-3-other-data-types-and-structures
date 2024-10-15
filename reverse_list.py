
def reverse_list(my_list):
    """
    Reverse the values in a list containing exactly two numbers.

    Input:
    lst (list): A list containing exactly two numbers.

    Returns:
    list: The list with its two values swapped.
    
    Example:
    --------
    >>> reverse_list([5, 10])
    [10, 5]
    >>> reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    """

    for i in range(len(my_list) // 2):
        (my_list[i], my_list[-(i+1)]) = (my_list[-(i+1)], my_list[i])

    return my_list