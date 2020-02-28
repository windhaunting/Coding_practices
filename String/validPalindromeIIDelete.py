#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:43:38 2018

@author: fubao
"""

# 680. Valid Palindrome II


'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

'''


class Solution(object):
    def validPalindromeII(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #1st Approach #1: Brute Force [Time Limit Exceeded]  T: O(n^2);  Space: O(n)

        # For each index i in the given string, let's remove that character, 
       # then check if the resulting string is a palindrome. If it is, (or if the original string was a palindrome),
       # then we'll return true
        
        for i in xrange(len(s)):
            t = s[:i] + s[i+1:]
            if t == t[::-1]: return True

        return s == s[::-1]




      #2nd  time  o(n)      ; space   O(1)
      #If the beginning and end characters of a string are the same (ie. s[0] == s[s.length - 1]), 
      #then whether the inner characters are a palindrome (s[1], s[2], ..., s[s.length - 2]) uniquely determines whether the entire string is a palindrome.
       
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))

        for i in xrange(len(s) / 2):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True