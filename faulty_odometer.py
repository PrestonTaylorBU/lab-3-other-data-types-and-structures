def calculate_distance_from_fault_odometer(faulty_reading):
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
    reading_as_str = str(faulty_reading)
    reading_difference = 0
    current_skipped_fives = 0

    # The digits to the left of a digit are the number of times the digit 5 was skipped
    for i, x in enumerate(reading_as_str):
        skipped_fives = current_skipped_fives
        if int(x) > 5:
            skipped_fives += 1

        reading_difference += skipped_fives * (10 ** (len(reading_as_str) - i - 1))

        current_skipped_fives *= 10
        current_skipped_fives += int(x)

    return faulty_reading - reading_difference

if __name__ == '__main__':
    faulty_reading = int(input("Enter the faulty reading from the odometer: "))

    print(f"The correct distance travelled is {calculate_distance_from_fault_odometer(faulty_reading)} miles")