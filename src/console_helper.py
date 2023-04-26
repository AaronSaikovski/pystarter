#!/usr/bin/env python
""" Standard console outputs with colours

Provides a helper module for displaying output with colours.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

"""Private color constants to print in the console constants for this module 
"""
__BLUE: str = '\033[94m'
__CYAN: str = '\033[96m'
__OK_GREEN: str = '\033[92m'
__WARNING: str = '\033[93m'
__ERROR: str = '\033[91m'
__ENDC: str = '\033[0m'
__BOLD: str = '\033[1m'
__UNDERLINE: str = '\033[4m'


def print_ok_message(message_string: str) -> None:
    """Prints an OK message using the console with the colour constant - __OK_GREEN

    Parameters
    ----------
    message_string : string
    
    Returns
    -------
    nothing - prints formatted output.
    """
    print(f'{__OK_GREEN}{message_string}{__ENDC}')

def print_warning_message(message_string: str) -> None:
    """Prints a Warning message using the console with the colour constant - __WARNING

    Parameters
    ----------
    message_string : string

    Returns
    -------
    nothing - prints formatted output.
    """
    print(f'{__WARNING}{message_string}{__ENDC}')

def print_error_message(message_string: str) -> None:
    """Prints an Error message using the console with the colour constant - __ERROR

    Parameters
    ----------
    message_string : string

    Returns
    -------
    nothing - prints formatted output.
    """
    print(f'{__ERROR}{message_string}{__ENDC}')


def print_confirmation_message(message_string: str) -> None:
    """Prints an confirmation message using the console with the colour constant - __BLUE

    Parameters
    ----------
    message_string : string
    
    Returns
    -------
    nothing - prints formatted output.
    """
    print(f'{__BLUE}{message_string}{__ENDC}')

def print_command_message(message_string: str) -> None:
    """Prints an command to run message using the console with the colour constant - __CYAN

    Parameters
    ----------
    message_string : string

    Returns
    -------
    nothing - prints formatted output.
    """
    print(f'{__CYAN}{message_string}{__ENDC}')


def print_bold_message(message_string: str) -> None:
    """Prints a bold message using the console with the colour constant - __BOLD

    Parameters
    ----------
    message_string : string

    Returns
    -------
    nothing - prints formatted output.
    """
    print(f'{__BOLD}{message_string}{__ENDC}')
    