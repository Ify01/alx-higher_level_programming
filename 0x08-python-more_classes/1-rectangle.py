#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """This class represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle class.
        
        Args:
            width (int): Represents the width of the rectangle.
            height (int): Represents the height of the rectangle.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get the width attribute."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width attribute."""
        self._validate_size(value, "width")
        self._width = value

    @property
    def height(self):
        """Get the height attribute."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height attribute."""
        self._validate_size(value, "height")
        self._height = value

    def _validate_size(self, value, attribute):
        """Validate that size is an integer and non-negative."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")
