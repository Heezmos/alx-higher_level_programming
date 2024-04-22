#!/usr/bin/python3
""" Base class for managing
geometric shapes """
import json
import turtle


class Base:
    """ Base class with utility methods for
    managing geometric shapes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the Base class
        instance with an optional ID """
        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts a list of dictionariesto a JSON string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of a list of
        objects to a file """
        LO_dict = []
        if list_objs is not None:
            LO_dict = [x.to_dictionary() for x in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(LO_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Returns a list from the JSON string representation """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance of the class and returns it """
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        elif cls.__name__ == "Square":
            inst = cls(1)
        else:
            return None
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances loaded from a file """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                content_read = f.read()
        except FileNotFoundError:
            return []
        list_of_dicts = cls.from_json_string(content_read)
        return [cls.create(**inst) for inst in list_of_dicts]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draws a list of rectangles and
        squares using the turtle module """
        for rec in list_rectangles:
            rec = rec.to_dictionary()
            turtle.up()
            turtle.setx(rec["x"])
            turtle.sety(rec["y"])
            turtle.down()
            turtle.fd(rec["width"])
            turtle.right(90)
            turtle.fd(rec["height"])
            turtle.right(90)
            turtle.fd(rec["width"])
            turtle.right(90)
            turtle.fd(rec["height"])
        for square in list_squares:
            size = square["size"]
            turtle.up()
            turtle.setx(square["x"])
            turtle.sety(square["y"])
            turtle.down()
            turtle.fd(size)
            turtle.right(90)
            turtle.fd(size)
            turtle.right(90)
            turtle.fd(size)
            turtle.right(90)
            turtle.fd(size)
            turtle.right(90)
