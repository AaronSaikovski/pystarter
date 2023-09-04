def inc(x):
    return x + 1


def dec(x):
    return x - 1


def test_inc():
    assert inc(3) == 4
    assert inc(5) == 6


def test_dec():
    assert dec(5) == 4
