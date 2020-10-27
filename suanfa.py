# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/5/26 13:17
"""
import time

'''
二分查找
'''


def binary_search(l, num):
    right = len(l) - 1
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if num == l[mid]:
            return mid
        elif num > l[mid]:
            left = mid + 1
        elif num < l[mid]:
            right = mid - 1
    return '没有找到'


#
# if __name__ == '__main__':
#     l = [11, 22, 33, 44, 55, 66]
#     print(erFenSearch(l, 66))


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
topK问题

'''


def top_sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp


def top_k_sort(li, k):
    heap = li[:k]
    n = len(li)
    # 建堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
    # 遍历
    for i in range(k, n - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    # 出数
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)


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
        merge(l, low, mid, high)
    return l


'''
希尔排序（插入排序）
'''

'''
计数排序（100以内，有相同数值）
'''

'''
桶排序
'''

'''
基数排序 （10个桶）
'''



'''
单例模式
'''
from functools import wraps


def single_ton(cls):
    _instance = {}

    @wraps(cls)
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return single


'''
斐波那契数列
'''
# def fib(max):
#     a, b = 0, 1
#     while max > 0:
#         a, b = b, a + b
#         max -= 1
#         yield a

# print([n for n in fib(10)])


'''
任意进制的转换
'''


def convString(num, base):
    rule = '0123456789ABCDE'
    if num < base:
        return rule[num]
    else:
        return convString(num // base, base) + convString(num % base, base)


"""
 硬币兑换最少(递归）
 """


def recDC(numList, change):
    minCoin = change
    # 如果找零在零钱中
    if change in numList:
        return 1
    for i in [c for c in numList if c < change]:
        minNum = 1 + recDC(numList, change - i)
        if minNum < minCoin:
            minCoin = minNum
    return minCoin


# 优化
def recDCopt(numList, change, knowChange):
    minCoin = change
    # 如果找零在零钱中
    if change in numList:
        knowChange[change] = 1
        return 1
    # 避免重复计算,直接返回最优解
    if knowChange[change] != 0:
        return knowChange[change]
    for i in [c for c in numList if c < change]:
        minNum = 1 + recDC(numList, change - i, knowChange)
        if minNum < minCoin:
            minCoin = minNum
            knowChange[change] = minCoin  # 找到最优解，记录
    return minCoin


"""
最大回文子串
dp[i][j] and dp[i-1]==dp[j+1]  ---> dp[i+1][j-1] 
i: start_index   j: end_index
"""


def long_sub(s):
    length = len(s)
    max_length = 1
    start_index = 0
    dp = [[False for _ in range(length)] for _ in range(length)]

    if not s:
        return
    # 单个字符肯定是回文
    for i in range(length):
        dp[i][i] = True

    for j in range(length):
        for i in range(j):
            if s[i] == s[j]:
                # 奇数  abaa
                if j - i < 3:
                    dp[i][j] = True
                # 偶数
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            # 判断是否是回文
            if dp[i][j]:
                current_length = j - i + 1
                # 判断最大长度
                if max_length < current_length:
                    max_length = current_length
                    # 起始位置
                    start_index = i
    return s[start_index:start_index + max_length]


if __name__ == '__main__':
    li = [133, 43, 545, 78, 75, 90, 32, 76, 33, 5, 8]
    # print(bubble_sort(li))
    # print(selection_sort(li))
    # print(insert_sort(li))
    # print(quick_sort(li, 0, len(li) - 1))
    # heap_sort(li)
    high = len(li)
    print(merge_sort(li, 0, high - 1))
    # h = convString(1, 16)
    # print(time.clock())

    # n = recDC([1, 5, 10, 25], 63, [0]*64)
    # n = {(i, w): 0 for i in range(10) for w in range(5)}
    # n = {1, 2, 4, 5}
    # n = long_sub('addsssffddasrvbvfgfdscsdfdg')
    # s = n
    # print(s)
