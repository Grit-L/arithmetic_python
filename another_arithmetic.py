# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/10/27 17:12
"""

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


'''
计数排序（100以内，有相同数值）
'''


def count_sort(li, max_num):
    tmp_li = [0 for _ in range(max_num+1)]
    # 数据归类
    for i in li:
        tmp_li[i] += 1
    # 清空原来列表
    li.clear()
    for ind, val in enumerate(tmp_li):
        for i in range(val):
            li.append(ind)
    return li


'''
桶排序
'''


def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建桶
    for var in li:
        # 放到几号桶 (max_num//n) 一个桶的取值范围
        ind = min(var//(max_num//n), n-1)
        # 添加到桶
        buckets[ind].append(var)
        # 保持桶内顺序 冒泡思想：从列表尾往前逐个比较
        for j in range(len(buckets[ind])-1, 0, -1):
            if buckets[ind][j] < buckets[ind][j-1]:
                buckets[ind][j], buckets[ind][j-1] = buckets[ind][j-1], buckets[ind][j]
            else:
                break
    li.clear()
    # 重新写回
    for buck in buckets:
        li.extend(buck)
    return li


'''
基数排序 （10个桶）
思想：键值优先级排序
'''


def radix_sort(li):
    num = max(li)
    # 排序次数 先个位 十位 逐渐往前
    t = 0
    # 次数 9 -》1  99-》2  1000-》4
    while 10**t <= num:
        buckets = [[] for _ in range(10)]
        for i in li:
            # 985 --> 985%10 =5 --> 985//10=98%10 =8 -->  985//100=9%10 =9
            var = (i // 10**t) % 10
            buckets[var].append(i)
        li.clear()
        # 重新写回li
        for buck in buckets:
            li.extend(buck)
        t += 1
    return li
