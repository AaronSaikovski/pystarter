"""
Generic logging module
"""
import functools
import logging

# set logging level
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# ******************************************************************************** #


def log(func):
    """
    Logging decorator
    source: https://ankitbko.github.io/blog/2021/04/logging-in-python/
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.debug("function {%f} called with args {%s}", func.__name__, signature)
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            # pylint: disable=logging-fstring-interpolation
            logger.exception(f"Exception in {func.__name__}. exception: {ex!s}")
            raise ex

    return wrapper


# ******************************************************************************** #

# usage of decorator
# @log
# def function test_func():
