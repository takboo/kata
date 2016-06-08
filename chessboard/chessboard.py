# usr/bin/python
# _*_ coding:utf-8 _*_

"""
Description:

Write a program that prints a chessboard with N rows and M columns with the following rules: The top left
cell must be an asterisk (*) Any cell touching (left, right, up or down) a cell with an asterisk must be
a dot (.) Any cell touching (left, right, up or down) a cell with a dot must be an asterisk.

A chessboard of 8 rows and 8 columns printed using these rules would be:

*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*

Input

A single line with two integers N and M separated by space. The number N will represent the number of rows
and M the number of columns.

Output

Return N lines each containing M characters with the chessboard pattern. Empty string if N, M or both are 0.
"""


def chessboard(s):
    """
    :param s: the string contains N row and M column, separated by whitespace
    :type s: str
    """
    if not s:
        return ""
    nums = s.split(" ")
    if len(nums) <= 1 or len(nums) > 2:
        return ""

    row = int(nums[0])
    column = int(nums[1])

    if not row or not column:
        return ""

    ret = []

    ret = ["\n" for i in range(row * (column + 1))]

    values = {".": "*", "*": "."}
    first = "*"
    column += 1
    for n in range(row):
        for m in range(column):
            if m == column - 1:
                continue
            if n - 1 >= 0:
                ret[n*column + m] = values[ret[(n - 1) * column + m]]
            elif m - 1 >= 0:
                ret[n*column + m] = values[ret[n * column + (m - 1)]]
            else:
                ret[n*column + m] = first

    return "".join(ret)[:-1]



