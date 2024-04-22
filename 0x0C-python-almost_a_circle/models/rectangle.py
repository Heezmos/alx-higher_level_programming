#!/usr/bin/python3
""" Defines a Rectangle class that
inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Retrieves the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieves the x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieves the y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of a
        rectangle
        """
        return self.__height * self.__width

    def display(self):
        """ Displays the rectangle
        pattern """
        for v_shift in range(self.__y):
            print()
        for height in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ Returns a string representation
        of the class """
        string = "[{:s}] ({:d})".format(type(self).__name__, self.id)
        string += " {:d}/{:d} ".format(self.__x, self.__y)
        string += "- {:d}/{:d}".format(self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """ Updates the class
        attributes """
        arg_count = len(args)
        if arg_count == 0:
            if "id" in kwargs.keys():
                super().__init__(kwargs["id"])
            if "width" in kwargs.keys():
                self.width = kwargs["width"]
            if "height" in kwargs.keys():
                self.height = kwargs["height"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]
        if arg_count > 0:
            super().__init__(args[0])
        if arg_count > 1:
            self.width = args[1]
        if arg_count > 2:
            self.height = args[2]
        if arg_count > 3:
            self.x = args[3]
        if arg_count > 4:
            self.y = args[4]

    def to_dictionary(self):
        """ Returns a dictionary representation of the object """
        dict_rec = {"x": self.__x, "y": self.__y, "id": self.id}
        dict_rec["width"] = self.__width
        dict_rec["height"] = self.__height
        return dict_rec
