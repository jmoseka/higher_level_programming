#!/usr/bin/python3
"""define a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    class that inherits from Base
    Attributes:
          width, height, x, y, id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the values passed to the object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getting width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getting height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getting x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getting y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """set the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print a rectangle"""
        for i in range(self.__y):
            print("")
        for column in range(self.__height):
                for j in range(self.__x):
                    print(" ", end="")
                for row in range(self.width):
                    print("#", end="")
                print("")

    def __str__(self):
        """updated rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """assign an argument to each attribute and
        assigns a key/value argument to attributes
        """
        nk_args = ["id", "width", "height", "x", "y"]
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
        """the dictionary representation"""
        dictionary = {"id": self.id, "width": self.__width,
                      "height": self.__height, "x": self.__x, "y": self.__y}
        return dictionary
