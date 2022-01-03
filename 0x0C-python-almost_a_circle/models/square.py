#!/usr/bin/python3
"""define a Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation with size"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading method"""
        return ("[square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter value"""
        return self.width

    @size.setter
    def size(self, value):
        """setting value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns attributes
        Each key represents an attribute to the instance
        """
        nk_args = ["id", "size", "x", "y"]
        i = 0
        length = len(args)
        if length > 0:
            for arg in range(length):
                setattr(self, nk_args[i], args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """the dictionary representation of a Square"""
        dictionary_s = {"id": self.id, "size": self.size,
                        "x": self.x, "y": self.y}
        return dictionary_s
