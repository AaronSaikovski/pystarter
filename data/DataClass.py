from dataclasses import dataclass

@dataclass(slots=True)
class SampleDataClass():
    """Summary of class here.

    Longer class information...
    Longer class information...

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def public_method(self) -> None:
        """Public method

        Args:
          likes_spam: Defines if instance exhibits this preference.
        """
        pass

    def __post_init__(self) -> None:
        """Post Init method

        Args:
          likes_spam: Defines if instance exhibits this preference.
        """
        pass
    