#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 00:45:01 2018

@author: fubao
"""



# 398. Random Pick Index      facebook

'''
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
'''


# reference http://rainykat.blogspot.com/2017/01/leetcodef-398-random-pick-indexdesgin.html

# brute force solution:

# iterate to get all the element in the nums array that equal to nums; put in the new array, randomly generate a target index;  ( all weight is 1)
#and return the index          or may not  put in the array), generate a random index and compare the element index (element == target) and return
#    O(N) time  (m) space

#2nd the better way to solve this?  use reservoir sampling;    use no extra space;    o(1) space
# http://rainykat.blogspot.com/2017/01/leetcodef-398-random-pick-indexdesgin.html

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        count, index = 0, 0
        for i, n in enumerate(self.nums):
            if n == target:
                count += 1
                rand = random.randint(1, count)
                if rand == count:
                    index = i

        return index
        
        

# Your Solution object will be instantiated and called as such:
nums =[1,2,3,3,3,3]
target = 3
obj = Solution(nums)
param_1 = obj.pick(target)
 
print ("idx: ", param_1)
        
        
        
        
        