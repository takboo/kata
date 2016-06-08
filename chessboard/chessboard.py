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
    row, column = map(int, s.split(" "))
    pattern = "*." * column
    return "\n".join([pattern[1: column + 1] if i % 2 else pattern[: column] for i in range(row)])




