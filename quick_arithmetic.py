# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/10/27 17:09
"""


'''
快排
'''


def quick_sort(li, start, end):
    if start >= end:
        return
    left = start
    right = end
    # 设中间值为第一个
    mid = li[left]
    while left < right:
        # 让右边游标往左移动，目的是找到小于mid的值，放到left游标位置
        while left < right and li[right] >= mid:
            right -= 1
        li[left] = li[right]
        # 让左边游标往右移动，目的是找到大于mid的值，放到right游标位置
        while left < right and li[left] < mid:
            left += 1
        li[right] = li[left]
    li[left] = mid
    # 递归处理左边的数据
    quick_sort(li, start, left - 1)
    # 递归处理右边的数据
    quick_sort(li, left + 1, end)
    return li


'''
堆排
时间复杂度：nlogn
'''


# 调整函数
def sift(li, low, high):
    """
    :param li:  排序列表
    :param low:  根节点
    :param high: 最后的叶子节点 预防下标溢出
    :return:
    """
    i = low  # 最开始指向根节点
    j = 2 * i + 1  # 叶子节点
    tmp = li[low]  # 堆顶存起来 用来比较
    while j <= high:  # 数组不越界 j位置有值
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果有有孩子(j+1 <= high)并且比较大(小）
            j = j + 1
        if li[j] > tmp:  # 如果子节点比根节点大(小）
            li[i] = li[j]
            i = j  # 往下比较一层
            j = 2 * i + 1
        else:  # tmp更大，把tmp放到i位置
            break
    li[i] = tmp  # 如果没有叶节点了 i是最后一级了


def heap_sort(li):
    n = len(li)
    # 构建堆，农村包围城市
    for i in range(n // 2 - 1, -1, -1):  # n --> n//2-1 子节点找父节点
        # i指向建堆时候调整部分的根下标
        sift(li, i, n - 1)  # high指向最后一个值，只是用来比较的
    # 挨个找数
    for i in range(n - 1, -1, -1):
        # i指向当前堆的最后一个位置
        li[0], li[i] = li[i], li[0]  # 建完堆后根节点是最大的，所以先进行交换
        sift(li, 0, i - 1)  # i-1是最新的high
    print(li)



'''
归并排序
'''


def merge(li, low, mid, high):
    """
    :param li:
    :param low:
    :param mid:
    :param high:
    :return:
    """
    i = low  # 前一半列表起始下标
    j = mid + 1  # 后一半列表起始下标
    ltmp = []  # 临时列表
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp  # 写回li


def merge_sort(l, low, h):
    if low < h:
        mid = (low + h) // 2
        merge_sort(l, low, mid)
        merge_sort(l, mid + 1, h)
        merge(l, low, mid, h)
    return l
