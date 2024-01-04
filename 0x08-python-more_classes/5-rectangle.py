#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, size):
        """Initialize a new rectangle.

        Args:
            size (int): The size of the new rectangle.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the rectangle."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the rectangle."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the rectangle with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
