def calculate_distance_from_faulty_odometer(faulty_reading):
    """
    Calculates the correct distance travelled from the reading of a fault odometer.
    The odometer skips the digit 5, so it goes from 4 to 6.

    Parameters:
    ----------
    faulty_reading: int
        The faulty reading from the odometer.

    Returns:
    -------
    int
        The correct distance travelled from the reading of the fault odometer.

    Example:
    --------
    calculate_distance_from_fault_odometer(6) # Outputs: 5
    """
    # The simplest way to calculate the correct distance is to realise that all the digits are in base 9 in the fault reading
    # So we convert the base 9 number to base 10, accounting for the numbers over 5.
    correct_reading = 0
    power = 0
    while faulty_reading > 0:
        current_digit = faulty_reading % 10
        faulty_reading //= 10

        if current_digit > 5:
            current_digit -= 1

        correct_reading += current_digit * (9 ** power)
        power += 1

    return correct_reading

if __name__ == '__main__':
    user_reading = int(input("Enter the faulty reading from the odometer: "))

    print(f"The correct distance travelled is {calculate_distance_from_faulty_odometer(user_reading)} miles")