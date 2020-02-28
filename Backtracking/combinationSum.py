#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:40:46 2018

@author: fubao
"""

#  39. Combination Sum



'''

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]

'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        '''
        #1st backtracking dfs   # reference https://www.youtube.com/watch?v=irFtGMLbf-s
        # [2, 3, 6, 7]  7, => 2(5) 22(3)  222(1) 2222(-1); 22223(skipped dfs); 223(0) (answer); 236(-4) < 0;  26() ; , 5,[2,3] 2 2
        #sort 
        candidates = list(set(candidates))
        candidates.sort()
        tmp = []
        res = []
        self.DFS(candidates, target, 0, tmp, res)
        return res
    
    def DFS(self, candidates, target, start, tmp, res):
        if target == 0:
            return res.append(tmp[:])
        for i in range(start, len(candidates)):
            if target < candidates[i]:           #positive integer,  reduce search  the rest of dfs
                return
            self.DFS(candidates, target-candidates[i], i, tmp+[candidates[i]], res)
            #tmp.pop(-1)
    '''
    
    
 
            
SolutionObj = Solution()
candidates = [2,2,6,3,7]
target = 10
print(SolutionObj.combinationSum(candidates, target))


# 40. Combination Sum II

'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

'''


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        #similar to combination I, but needs to modify the backtracking starting from each one
        
        #
        #candidates = list(set(candidates))
        candidates.sort()
        tmp = []
        res = []
        self.DFS(candidates, target, 0, tmp, res)
        return res
        
    def DFS(self, candidates, target, start, tmp, res):
        if target == 0:
            return res.append(tmp[:])
        prev = -1
        for i in range(start, len(candidates)):
            if prev != candidates[i]:                         #remove the duplicate combinations final result
                if target < candidates[i]:
                    return
                self.DFS(candidates, target-candidates[i], i+1, tmp+[candidates[i]], res)  # and use next element only; i+1  instead of i
                prev = candidates[i]
                


# combinationSum IV  Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.                
# using DP  reference the DP folder
                
'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
             
                
nums = [4, 2, 1]
target = 32

ans:  39882198

# very time-consuming

'''

class Solution(object):
    
    ans = 0
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 1st recursive way;     TLE,  soluton should be correct
        nums.sort()
        
        self.DFS(nums, target)
        
        return self.ans
        
    def DFS(self, nums, target):
        if target == 0:
            self.ans += 1
            #print ("ans: ", self.ans)
            return self.ans
        for i in range(0, len(nums)):       # not from start?
            if target < nums[i]:
                return
            self.DFS(nums, target-nums[i])  # and use next element only; i+1  instead of i
            

        #2nd method use DP method:
        '''
    
        DP O(n * target)               # n is the number
        
        f[ v ] = sum( f[v - x [j]] )
        
        
        
        f[4] = (if first number is 3, then there are f[4-3] cases after 3) + (if first number is 2, then there are f[4-2] cases after 2) + (if first number is 1, then there are f[4-3] cases after 1)
        (3, 1) + (2, 1,1) | (2, 2) + (1, 1,1) | (1, 1,2) | (1, 2,1) | (1, 3)
        
        f(4) = f(1) + f(2) + f(3)
        = 1 + f(0) + f(1) + f(2) + f(1) + f(0)
        = 1 + 1 + 1 + 2 + 1 + 1
        = 7
        '''
        count = [0] * (target + 1)
            count[0] = 1
            
            for i in xrange(1, target+1):
                for x in nums:
                    if i >= x:
                        count[i] += count[i-x]
                        
            return count[target]
    

# reference
