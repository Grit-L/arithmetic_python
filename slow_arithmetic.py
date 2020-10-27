# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/10/27 17:09
"""


'''
冒泡排序 O(n)
'''


def bubble_sort(l):
    length = len(l)
    # 一共多少数
    for i in range(length - 1):
        # 对比次数
        for j in range(length - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


'''
选择排序
'''


def selection_sort(li):
    length = len(li)
    for i in range(length - 1):
        postion = i
        min_v = li[i]
        for j in range(i, length):
            if li[j] < min_v:
                min_v = li[j]
                postion = j
        li[i], li[postion] = li[postion], li[i]
    return li


'''
插入排序
'''


def insert_sort(li):
    for i in range(1, len(li)):
        current_value = li[i]  # 插入项/对比项
        index = i
        # 一直比到第一项，位置挪动
        while index > 0 and current_value > li[index - 1]:
            li[index] = li[index - 1]  # 循环对比，移动
            index = index - 1  # 找到大于的值,记住下标
        li[index] = current_value
    return li


'''
希尔排序（插入排序 分成len(li)//2 组进行插入）
'''


def insert_sort_gap(li, gap):
    n = len(li)
    for i in range(gap, n):
        ind = i
        cur = li[ind]
        while ind > 0 and cur > li[ind-gap]:
            li[ind] = li[ind-gap]
            ind = ind - gap
        li[ind] = cur


def shell_sort(li):
    # d 指的分的组数
    d = len(li) // 2
    # 4 -》 2 -》 1
    while d > 0:
        insert_sort_gap(li, d)
        d //= 2
    return li
