""" Standard console outputs with colours
Provides a helper module for displaying output with colours.
"""

"""color constants to print in the console constants for this module 
"""
__BLUE: str = "\033[94m"
__CYAN: str = "\033[96m"
__OK_GREEN: str = "\033[92m"
__WARNING: str = "\033[93m"
__ERROR: str = "\033[91m"
__ENDC: str = "\033[0m"
__BOLD: str = "\033[1m"
__UNDERLINE: str = "\033[4m"

# ******************************************************************************** #

def print_ok_message(message_string: str) -> None:
    """Prints OK message - __OK_GREEN

    Parameters
    ----------
    message_string : string

    Returns
    -------
    nothing - prints formatted output.
    """
    print(f"{__OK_GREEN}{message_string}{__ENDC}")

# ******************************************************************************** #

def print_warning_message(message_string: str) -> None:
    """Prints Warning message - __WARNING

    Parameters
    ----------
    message_string : string

    Returns
    -------
    nothing - prints formatted output.
    """
    print(f"{__WARNING}{message_string}{__ENDC}")

# ******************************************************************************** #

def print_error_message(message_string: str) -> None:
    """Prints Error message  - __ERROR

    Parameters
    ----------
    message_string : string

    Returns
    -------
    nothing - prints formatted output.
    """
    print(f"{__ERROR}{message_string}{__ENDC}")

# ******************************************************************************** #

def print_confirmation_message(message_string: str) -> None:
    """Prints confirmation message - __BLUE

    Parameters
    ----------
    message_string : string

    Returns
    -------
    nothing - prints formatted output.
    """
    print(f"{__BLUE}{message_string}{__ENDC}")

# ******************************************************************************** #

def print_command_message(message_string: str) -> None:
    """Prints acommand message - __CYAN

    Parameters
    ----------
    message_string : string

    Returns
    -------
    nothing - prints formatted output.
    """
    print(f"{__CYAN}{message_string}{__ENDC}")

# ******************************************************************************** #

def print_bold_message(message_string: str) -> None:
    """Prints a bold message - __BOLD

    Parameters
    ----------
    message_string : string

    Returns
    -------
    nothing - prints formatted output.
    """
    print(f"{__BOLD}{message_string}{__ENDC}")

# ******************************************************************************** #
