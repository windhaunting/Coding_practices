#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 17:20:28 2018

@author: fubao
"""

#  http://blog.csdn.net/qian2729/article/details/50531582

# 43. Multiply Strings

#  facebook

'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

'''
# reference:

http://blog.csdn.net/qian2729/article/details/50531582


# https://www.programcreek.com/2014/05/leetcode-multiply-strings-java/


#

 1. m位的数字乘以n位的数字的结果最大为m+n位：
999*99 < 1000*100 = 100000，最多为3+2 = 5位数。
2. 先将字符串逆序便于从最低位开始计算。

'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # make sure size of num2 is bigger than size of num1
        if len(num1) > len(num2):
            return self.multiply(num2,num1)
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                ans[i + j] += int(num1[i]) * int(num2[j])
        c = 0
        for i in range(len(ans)):
            ans[i] += c
            ans[i],c = ans[i] % 10, ans[i] / 10
        while c > 0:
            ans.append(c % 10)
            c = c / 10
        index = len(ans) - 1
        while index > 0 and ans[index] == 0:
            index -= 1
        return ''.join([str(x) for x in ans[0:index + 1]][::-1])