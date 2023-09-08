class StandardClass:
    """Summary of class here.

    Longer class information...
    Longer class information...

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    # ******************************************************************************** #

    def __init__(self, someintvalue: int) -> None:
        """Initializes the instance based on spam preference.

        Args:
          someintvalue: some int value
        """
        self.someintvalue = someintvalue

    # ******************************************************************************** #

    def return_some_value(self) -> int:
        """Public method

        Args:
          likes_spam: Defines if instance exhibits this preference.
        """
        return self.someintvalue

    # ******************************************************************************** #
