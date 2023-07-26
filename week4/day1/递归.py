# -*- coding: UTF-8 -*-
__author__ = 'zhangyuanyuan_vendor@sensetime.com'


# 用递归实现阶乘

def recursion(n):
    if n == 1:
        return 1
    return n * recursion(n - 1)


print(recursion(5))


# 斐波那契数列：0,1,1,2,3,5,8,13,21,34....

def fibo(n):

    if n >= 2:
        return fibo(n-1) + fibo(n-2)
    else:
        return n


print(fibo(8))
