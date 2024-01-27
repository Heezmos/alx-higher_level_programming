def print_list(my_list = []):

    length_list = len(my_list)

    new_range = range(length_list)

    for num in new_range:
        print(num)

    print("{}".format(length_list))

print_list()
