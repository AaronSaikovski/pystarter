"""
Profiling function helper - used to profile function performance
"""

import functools
import time

# ******************************************************************************** #


def profile_func(func):
    """
    Profile Logging decorator
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed time: {(end - start) * 1000:.3f}ms")

    return wrapper


# ******************************************************************************** #

# usage of decorator to measure function performance
# @profile_func
# def add (num1: int, num2: int) :
# 	print (f"Add {num1} and {num2}")
# 	return num1 + num2
