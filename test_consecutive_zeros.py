from consecutive_zeros import consecutive_zeros

def test_consecutive_zeros():
    assert consecutive_zeros("") == 0
    assert consecutive_zeros("1") == 0

    assert consecutive_zeros("0") == 1
    assert consecutive_zeros("00") == 2
    assert consecutive_zeros("1001110010") == 2

    assert consecutive_zeros("10000001110010") == 6
