#!/usr/bin/env python3

# MIT License

# Copyright (c) 2025 Aaron Saikovski

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" Short description of this Python module.

Longer description of this module.

"""
import os

from dotenv import load_dotenv

import sample_data.standardclass as standardclass
import sample_package.sample_module as sample_module
import utils.console_helper as console
import utils.logging_helper as logging
import utils.profiling_helper as profiler

load_dotenv()
    
# ******************************************************************************** #


@logging.log
def add_nums_test(num1: int, num2: int) -> int:
    """adds two numbers as a test

    Args:
        num1 (int): Value 1
        num2 (int): Value 2_description_

    Returns:
        int: sum of numbers
    """
    return num1 + num2


# ******************************************************************************** #


@profiler.profile_func
def main():
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/


    """

    console.print_ok_message("** This is the main method.** ")
    
    # Load from .env file
    env_value = os.getenv("SOME_VALUE","no value set")
    print(f"From .env file: {env_value}")

    nums_test = add_nums_test(50, 50)
    print(f"Adding nums: {nums_test}")

    sample_class = standardclass.StandardClass(100)
    print(f"From Class instance: {sample_class.return_some_value()}")

    print(f"From module: {sample_module.sample_function()}")


# ******************************************************************************** #

if __name__ == "__main__":
    main()
