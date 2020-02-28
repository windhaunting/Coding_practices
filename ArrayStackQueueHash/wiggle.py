#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 23:41:14 2018

@author: fubao
"""


# check sorting,  quicksort partition idea;
# and three-way partition idea

#324. Wiggle Sort II
'''

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

'''

def wiggleSort(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        '''
        #1st idea is to sort the array, and then get the median position;
        next we fetch the first element in the closest left of median position, and the closest right position
        of median to put in a new array, then the second closest left, the second closest right, on and so on.
        
        
        1. 对原数组排序，得到排序后的辅助数组snums

        2. 对原数组的偶数位下标填充snums的末尾元素

        3. 对原数组的奇数位下标填充snums的末尾元素
        '''
        
        nums = sorted(nums)
        print ("nums: ", nums)
        
        midInd = int(len(nums)/2)
        i = midInd-1
        ans = []
        while (i> 0):
            ans.append(nums[i])
            ans.append(nums[len(nums)-i])
            i -= 1
        
        ans.append(nums[0])
        ans.append(nums[midInd])
        nums = ans[::]
        print ("ans: ", ans, nums)
        
nums = [1,5,1,1,6,4]
nums = [1, 3, 2, 2, 3, 1]
nums = [1,5,1,1,6,4]
wiggleSort(nums)



# second way:

https://leetcode.com/problems/wiggle-sort-ii/discuss/125558/O(n)-time-+-O(1)-space-3-way-partition-beats-99.4-NO-virtual-index


https://en.wikipedia.org/wiki/Dutch_national_flag_problem#Pseudocode

