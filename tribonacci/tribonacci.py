# usr/bin/python
# _*_ coding:utf-8 _*_


def tribonacci(signature, n):
    """
    :param signature:
    :type signature:list
    :param n:
    :return:
    """

    for i in range(n):
        signature.append(sum(signature[i:3 + i]))

    return signature[:n]