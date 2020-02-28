#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:54:24 2018

@author: fubao
"""



# Leetcode: 340. Longest Substring with At Most K Distinct Characters


'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,
T is "ece" which its length is 3.


'''

'''

# reference: http://buttercola.blogspot.com/2016/06/leetcode-340-longest-substring-with-at.html
Understand the problem:
The problem is very similar to the Leetcode question 3 (Longest Substring Without Repeating Characters). 

The key idea of the solution is to use two pointers to maintain a "sliding window".
 We also use a HashMap to store all the characters in the window. Each time we move forward the "start" pointer and
 increase the size of the sliding window until the size of the window is greater than K. Then we can easily calculate 
 the size of the window which contains at most K distinct characters. The next step is to shrink the window by moving forward 
 the "end" pointer. In order to get the maximum window size, we must move the minimum steps of the end pointer.
 So each step we move the end pointer, we need to update the map and remove the character out of the sliding window.
 The stop condition is that when the window size is again equal to the K, which means the window contains K distinct characters. 
 That's the minimum steps we need to move forward the end pointer. 

The only trick here is we need to check at the last that if the start pointer is out of boundary, we still need to check 
if the largest window size. That's a common trick for major string w/ two pointer problems.

'''

# reference: http://buttercola.blogspot.com/2016/06/leetcode-340-longest-substring-with-at.html


class Solution:
    # @param s : A string
    # @return : An integer
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s or not k:
            return 0
        if len(s) < k:
            return len(s)
        right, length = 0, 0
        sourceHash = {}
        for left in range(len(s)):
            while len(sourceHash) <= k and right < len(s):
                if s[right] not in sourceHash:
                    sourceHash[s[right]] = 1
                else:
                    sourceHash[s[right]] += 1
                right += 1
            if len(sourceHash) == k + 1 and right - left - 1 > length:
                length = right - left - 1
            elif right >= len(s) and right - left > length:
                length = right - left
                
            sourceHash[s[left]] -= 1
            if sourceHash[s[left]] == 0:
                del sourceHash[s[left]]
        
        return length

