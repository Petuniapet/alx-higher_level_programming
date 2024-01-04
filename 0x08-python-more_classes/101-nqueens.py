#!/usr/bin/python3
class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(side, side)

    @property
    def side(self):
        return self.width

    @side.setter
    def side(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return '[Square] {0}'.format(self.width)

    def __repr__(self):
        return 'Square({0})'.format(self.width)

# Example usage:
# s = Square(4)
# print(s)  # Output: [Square] 4
