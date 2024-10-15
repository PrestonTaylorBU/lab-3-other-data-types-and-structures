def consecutive_zeros(input_string):
    """
    Calculates the number of consecutive zeros in the input string.

    Parameters:
    ----------
    input_string: str
        A string containing either 0s or 1s

    Returns:
    -------
    int
        The number of consecutive zeros in the input string

    Example:
    --------
    consecutive_zeros("10100001000") # Outputs: 4
    """
    result = 0
    current = 0
    for c in input_string:
        if c == '0':
            current += 1
            result = max(current, result)
        else:
            current = 0

    return result

if __name__ == '__main__':
    user_string = input("Enter a string containing 0s and 1s: ")

    print(f"The number of consecutive zeros in the string is {consecutive_zeros(user_string)}")