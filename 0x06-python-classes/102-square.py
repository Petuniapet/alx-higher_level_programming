#!/usr/bin/python3
class Square:
    """
    This is the Square module.

    Attributes:
        __size (int or float): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int or float): The size of the square.
        """
        if type(size) not in [int, float]:
            raise TypeError('size must be a number')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """
        Less than comparator for squares.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if the area of self is less than the area of other, False otherwise.
        """
        return self.area() < other.area()

    # ... (other special methods)

    def __ge__(self, other):
        """
        Greater than or equal comparator for squares.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if the area of self is greater than or equal to the area of other, False otherwise.
        """
        return self.area() >= other.area()
