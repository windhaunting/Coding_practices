#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 23:07:27 2018

@author: fubao
"""


# 456. 132 Pattern  stack


'''
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

'''


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #1st TLE naive way to check every triple ai, aj, ak
        
        #2nd TLE it only find true or false to the question, so we need to check any triple exist fast;  O(N^2) time. find the smallest element before aj, the find the middle number ak to exist betwee ai and aj
        minVal = 2**32
        for j in range(0, len(nums)):
            minVal = min(minVal, nums[j])
            for k in range(j+1, len(nums)):
                if minVal < nums[k] and nums[k] < nums[j]:
                    return True
        return False
                
        
        #3rd use stack;
        # https://leetcode.com/problems/132-pattern/solution/