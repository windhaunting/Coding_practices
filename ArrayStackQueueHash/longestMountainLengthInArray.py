#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:49:02 2018

@author: fubao
"""

#
'''
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
'''


class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        '''
        #1st use naive way to get each mountain shape one by one element as starting point. time complexity o(n^2)
        
        #2nd reduce time complexity by o(n) to only continue iterating next starting point using the first iteration's end point.
        #use two pointer to denote. start, end
        
        st = 0       # start point
        end = 0
        L = len(A)
        ansLen = 0
        decFlag = 0
        incFlag = 0
        while (end < (L-1)):
            if A[end] < A[end+1]:
                incFlag = 1
                if incFlag == 1 and decFlag == 1:    # terminate; find a mountain
                    st = end
                decFlag = 0
            elif A[end] > A[end+1]:
                decFlag = 1
                if incFlag == 0:
                    st = end+1
                    decFlag = 0
            else:
                decFlag = 0
                incFlag = 0
                st = end+1
            if incFlag == 1 and decFlag == 1 and (end == L-2 or (end-st+1) >=2):    # END ; find a mountain
                ansLen = max(ansLen, end-st+2)
            end += 1
        return ansLen
        '''
        N = len(A)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]: #if base is a left-boundary
                #set end to the peak of this potential mountain
                while end+1 < N and A[end] < A[end+1]:
                    end += 1

                if end + 1 < N and A[end] > A[end + 1]: #if end is really a peak..
                    #set 'end' to right-boundary of mountain
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                    #record candidate answer
                    ans = max(ans, end - base + 1)
                    print ("ans: ", ans, base, end)
            base = max(end, base + 1)

        return ans
    