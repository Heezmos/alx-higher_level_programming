#!/usr/bin/python3
# function that prints all integers of a list.
def print_list_integer(my_list=[]):
    for num in range(len(my_list)):
        print("{:d}".format(my_list[num]))
