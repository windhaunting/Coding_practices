#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:33:04 2018

@author: fubao
"""


#38. Count and Say


'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

'''



# class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sn = "1"
        res = sn
        k = 1
        while(k < n):
            l = len(sn)
            j = 0
            res = ""
            for i in range(0, l-1):
                if sn[i] != sn[i+1]:
                    res += str(i-j+1) + sn[i]
                    j = i+1

            res += str(l-j) + sn[-1]
            sn = res
            k += 1
        return res
        
    
    
    