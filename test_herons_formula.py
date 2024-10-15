import pytest
from herons_formula import herons_formula

def test_herons_formula_positive():
    assert herons_formula(0, 0, 0) == 0.0

    assert herons_formula(3, 4, 5) == 6.0
    assert herons_formula(5, 4, 3) == 6.0
    assert herons_formula(4, 5, 3) == 6.0

def test_herons_formula_negative():
    with pytest.raises(ValueError):
        herons_formula(-1, 0, 0)

    with pytest.raises(ValueError):
        herons_formula(0, -1, 0)

    with pytest.raises(ValueError):
        herons_formula(0, 0, -1)