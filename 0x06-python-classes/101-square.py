#!/usr/bin/python3
class Square:
    """
    This is the Square module.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        if type(position) is not tuple or len(position) != 2 or \
                type(position[0]) is not int or type(position[1]) is not int \
                or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        int: The size of the square.
        """
        return self.__size

    # ... (other getter and setter methods)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the specified position.

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
