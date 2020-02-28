#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 23:34:30 2018

@author: fubao
"""


#  3. Longest Substring Without Repeating Characters


'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        '''
        #1st my idea, using two pointer and hash table to trace the index; when there is repetition, compare the max length, and update i, j
        # o(n)
        if len(s) <= 1:
            return len(s)
        
        dic = {}
        i = 0
        j = 1
        maxLen = 1
        for ind, c in enumerate(s):
            cur = c
            if cur not in dic:
                dic[c] = ind
                j = ind+1
                
            else:
                preInd = dic[cur]
                
                #print ('j-i+1: ', j)
                maxLen = max(maxLen, j-i)
                i = preInd+1
        return maxLen
        
        '''
        #2nd use previous and current index value to compare 
        #  "jxdlnaaij", "bbtablud", "pwwkew", "tmmzuxt"
        i = 0
        j = i
        if len(s) <= 1:
            return len(s)
        prevRepetitionInd = 0
        maxLen = 0
        dic = {}
        for ind in range(0, len(s)):
            
            cur = s[ind]
            if cur not in dic:
                dic[cur] = ind
                j = ind
            else:
                if dic[cur] >= prevRepetitionInd:
                    maxLen = max(maxLen, j-i+1)
                    prevRepetitionInd = dic[cur]
                    i = prevRepetitionInd + 1
                else:
                    j = ind
                dic[cur] = ind

            prev = cur
        #print ('i, j: ', maxLen, j, i)
        return max(maxLen, j-i+1)
        

