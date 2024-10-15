import pytest
from faulty_odometer import calculate_distance_from_faulty_odometer

def test_calculate_distance_from_faulty_odometer_positive():
    assert calculate_distance_from_faulty_odometer(4) == 4
    assert calculate_distance_from_faulty_odometer(6) == 5
    assert calculate_distance_from_faulty_odometer(16) == 14
    assert calculate_distance_from_faulty_odometer(2004) == 1462

def test_calculate_distance_from_faulty_odometer_negative():
    assert calculate_distance_from_faulty_odometer(-1) == 0