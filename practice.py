# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/10/27 17:11
"""


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
        top_sift(heap, i, k - 1)
    # 遍历
    for i in range(k, n - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            top_sift(heap, 0, k - 1)
    # 出数
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        top_sift(heap, 0, i - 1)


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



'''
网格M*N从底往对角一共有几种走法 一次只能走一格

'''


# def go_count(m, n):
#
#     if m == 1 or n == 1:
#         total = 1
#     else:
#         total = go_count(m-1, n) + go_count(m, n-1)
#     return total

# print(go_count(10,9))



'''
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

例如：下面的二维数组就是每行、每列都递增排序。如果在这个数组中查找数字7，则返回true；
如果查找数字5，则由于数组不含该数字，返回false。
'''


def solution(l, num):
    m = len(l)
    n = len(l[0])
    # r:行 c:列
    r = 0
    c = n
    while r <= m and c > 0:
        target = l[r][c]
        if target == num:
            return True
        elif target > num:
            c -= 1
        else:
            r += 1
    return False


'''
最长无重复子串
'''


def lengthOfLongestSubstring(s: str) -> int:
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    n = len(s)
    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    rk, ans = -1, 0
    for i in range(n):
        if i != 0:
            # 左指针向右移动一格，移除一个字符
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:
            # 不断地移动右指针
            occ.add(s[rk + 1])
            rk += 1
        # 第 i 到 rk 个字符是一个极长的无重复字符子串
        ans = max(ans, rk - i + 1)
    return ans
