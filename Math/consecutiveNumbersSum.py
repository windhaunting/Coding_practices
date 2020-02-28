#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 21:48:28 2018

@author: fubao
"""


# 829. Consecutive Numbers Sum

'''
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.

'''

'''
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.

'''



class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        '''
        #1st TLE problem  naive way; check each element from 1 up to N and then judge the viability
        # then check from 2 up to N, then from 3 up to N  and so on.
        # time complexity:  O(N^2)
        waysNum = 0
        for i in range(0, N+1):
            tmpSum = 0
            for j in range(i+1, N+1):
                tmpSum += j
                if tmpSum == N:
                    waysNum += 1
                    break
        return waysNum
        '''
    
        #2nd  TLE reference : https://leetcode.com/problems/consecutive-numbers-sum/solution/
        '''
        ans = 0
        for k in xrange(1, N + 1):
            if 2*N % k == 0:
                y = 2 * N / k - k - 1
                if y % 2 == 0 and y >= 0:
                    ans += 1
        return ans
    
        '''
        
        #3rd  reference : https://leetcode.com/problems/consecutive-numbers-sum/solution/
        while N & 1 == 0:
            N >>= 1

        ans = 1    
        d = 3
        while d * d <= N:
            e = 0
            while N % d == 0:
                N /= d
                e += 1
            ans *= e + 1
            d += 2

        if N > 1: ans *= 2
        return ans
    
    
