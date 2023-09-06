#1/usr/bin/python3
"""Define class LockedClass"""


class LockedClass:
    """prevents from creating new instance attribute except for first_name"""

    __slots__ = ["first_name"]

    def __init__(self):
        """create new instance of LockedClass"""

        self.first_name = "first_name"
