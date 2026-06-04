from pystarter.app import add_nums_test


def test_add_nums_test():
    assert add_nums_test(1, 2) == 3
    assert add_nums_test(-1, 1) == 0
    assert add_nums_test(0, 0) == 0
