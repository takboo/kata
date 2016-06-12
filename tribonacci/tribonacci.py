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
        signature.append(sum(signature[:-3]))

    return signature[:n]

