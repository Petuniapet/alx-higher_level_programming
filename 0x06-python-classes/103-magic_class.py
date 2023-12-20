#!/usr/bin/python3
import math

class MagicClass:
    """
    This is the MagicClass module.

    Attributes:
        __radius (int or float): The radius of the MagicClass instance.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance.

        Args:
            radius (int or float): The radius of the MagicClass instance.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the MagicClass instance.

        Returns:
            float: The area of the MagicClass instance.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the MagicClass instance.

        Returns:
            float: The circumference of the MagicClass instance.
        """
        return 2 * math.pi * self.__radius
