#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 18:59:24 2018

@author: fubao
"""


#  647. Palindromic Substrings
'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
'''


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #1st naive way. get all the substring and check whether it's palindromic and count the number of substring palindromic.
        # too time-consuming. O(2^n) time.
        
        '''
        #TLE  o(n^3)  2nd DP. because it's the number of sth, and it reminds me of the DP.
        # e.g. cbbc,   bb is a palindromic,  we just need to judge the left and right part of this substring.
        # it has optimal substructing, and overlapping subproblem property
        
        # DP[i] indicates the number of substring ending at index i
        #DP[i] = sum(DP[j]) for j from 0 to i
        
        # 'abba',   'abc'
        def judgePalindrome(s):
            i = 0
            j = len(s)-1
            while (i < j):
                if s[i] != s[j]:
                    return 0
                i += 1
                j -= 1
            return 1
        
        n = len(s) 
        DP =[0] * n 
        for i in range(0, n):
            for j in range(0, i+1):
                #print ("i, j: ", i, j, s[j:i+1])
                if judgePalindrome(s[j:i+1]):                  # this would add more complexity, and make this solution TLE
                    DP[i] += 1
        #print ("DP: ", DP)
        return sum(DP)
        '''
        
        # 3rd use DP; reduce to O(n^2). 
        # define DP[i][j] is the palindrome or not between index i and j.
        # If s[i] == s[j] and dp[i+1][j-1] is palindrome, then DP[i][j] is also a palindrome
        n = len(s) 
        DP =[[0 for i in range(0, n)] for i in range(0, n)]         # twop pairs of brackets [[]]
        ans = 0
        #print ("dddDP: ", DP)

        for i in range(0, n):
            for j in range(0, i+1):
                #print ("i, j: ", i, j, s[j:i+1])
                if (s[i] == s[j] and ((i-j <= 2) or (DP[j+1][i-1]==1))):
                    #if 0 <i<n and 0<=j<n-1:
                        #print ("aaaai, j: ", i, j, s[i], s[j], j+1, i-1, DP[j+1][i-1])
                    DP[j][i] = 1
                    ans += 1
                    #print ("ttDP: ", i, j, DP, s[i], s[j])
        return ans
                                             
        #4th method reference  https://leetcode.com/problems/palindromic-substrings/solution/   or 
        # http://www.cnblogs.com/grandyang/p/7404777.html;      or   https://blog.csdn.net/MebiuW/article/details/76557629
        # expanding around s[i] left or right, if the palindrome is odd, s[i] is the center of palindrome.  The palindrome is even, s[i], s[i+1] are the center of the palindrome.
    
        