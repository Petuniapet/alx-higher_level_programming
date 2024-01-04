#!/usr/bin/python3
class Rectangle:
    count = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.count += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.__width, self.__height)

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.__width == other.width and self.__height == other.height

    def __ne__(self, other):
        return not self.__eq__(other)

    def __del__(self):
        Rectangle.count -= 1
        print("Bye rectangle...")

    def __str__(self):
        return '[Rectangle] {0}/{1}'.format(self.__width, self.__height)

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("unsupported operand type(s) for <: 'Rectangle' and {}".format(type(other)))
        return self.area() < other.area()

    def __le__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("unsupported operand type(s) for <=: 'Rectangle' and {}".format(type(other)))
        return self.area() <= other.area()

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("unsupported operand type(s) for >: 'Rectangle' and {}".format(type(other)))
        return self.area() > other.area()

    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("unsupported operand type(s) for >=: 'Rectangle' and {}".format(type(other)))
        return self.area() >= other.area()

# Example usage:
# r1 = Rectangle(3, 4)
# r2 = Rectangle(2, 6)
# print(r1 < r2)  # Output: False
# print(r1 > r2)  # Output: True

