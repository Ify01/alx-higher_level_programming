#!/usr/bin/python3

"""A module that defines a square."""

class Square:
    """A class that represents a square.

    Attributes:
        __size (int): The side length of the square.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
            Args:
                size (int): The side length of the square.
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than zero.

        area(self): Calculates the area of the square.
            Returns:
                int: The area of the square.
        """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The side length of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
