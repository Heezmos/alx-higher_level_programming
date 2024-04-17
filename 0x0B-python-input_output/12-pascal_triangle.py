#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to
    the specified
    number of rows.

    Pascal's Triangle is a mathematical triangle
    where each number is
    the sum of the two numbers directly above it.
    It is used in
    combinatorics and various mathematical and
    scientific applications.

    Args:
        n (int): The number of rows to generate in
        the triangle.

    Returns:
        list: A list of lists representing Pascal's
        Triangle, with each
              inner list containing the numbers of a row.
              For example, when n=3, the output is [[1],
              [1, 1], [1, 2, 1]].
              An empty list is returned
              when n is less
              than or equal to 0.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
