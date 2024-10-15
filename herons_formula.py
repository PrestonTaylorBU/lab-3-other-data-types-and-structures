import math

def herons_formula(a, b, c):
    """
    Calculates the area of a triangle using Heron's formula.

    Parameters:
    ----------
    a, b, c: float
        The individual side lengths of a triangle.

    Returns:
    -------
    float
        The area of the triangle with a, b and c as the side lengths

    Example:
    --------
    remove_duplicates(3, 4, 5)  # Output: 6.0
    """
    if a < 0 or b < 0 or c < 0:
        raise ValueError("The side lengths cannot be negative.")

    s = (a + b + c) / 2

    # Heron's formula: sqrt(s * (s - a)(s - b)(s - c))
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == '__main__':
    print("--- Triangle area calculator using Heron's formula ---")

    first_side = float(input("Enter the first side length: "))
    second_side = float(input("Enter the second side length: "))
    third_side = float(input("Enter the third side length: "))

    print(f"The area of the triangle is {herons_formula(first_side, second_side, third_side)}cm^2")