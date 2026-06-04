from pystarter.sample_data import standardclass


def test_class():
    """tests the class"""
    test_value: int = 1000
    test_class = standardclass.StandardClass(test_value)
    assert test_class.return_some_value() == test_value
