#!/usr/bin/python3
""" Defines a Square class that inherits
from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits
    from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a Square instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Retrieves the size value
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the Square
        attributes """
        arg_count = len(args)
        if arg_count == 0:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "size" in kwargs.keys():
                self.size = kwargs["size"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]
        if arg_count > 0:
            self.id = args[0]
        if arg_count > 1:
            self.size = args[1]
        if arg_count > 2:
            self.x = args[2]
        if arg_count > 3:
            self.y = args[3]

    def __str__(self):
        """ Returns a string representation
        of the class """
        string = "[{:s}] ({:d})".format(type(self).__name__, self.id)
        string += " {:d}/{:d} ".format(self.x, self.y)
        string += "- {:d}".format(self.size)
        return string

    def to_dictionary(self):
        """ Returns a dictionary representation
        of the object """
        dict_rec = {"x": self.x, "y": self.y, "id": self.id}
        dict_rec["size"] = self.size
        return dict_rec
