from pystarter.utils.profiling_helper import profile_func


@profile_func
def _sample_func():
    return 42


def test_profile_func_returns_value():
    assert _sample_func() == 42
