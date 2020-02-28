#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 00:40:28 2018

@author: fubao
"""

#  46. 47.  Permutations I, II

# https://leetcode.com/problems/permutations/discuss/18239


# similar problems: Subsets, Permutations, Combination Sum, Palindrome Partioning; 377. Combination Sum IV (DP)

'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    '''
    dfs(0, [1,2,3], [])
    |- dfs(1, [2,3], [1])
        |- dfs(2, [3], [1,2])
            |- ...
        |- dfs(2, [2], [1,3])
            |- dfs(3, [], [1,3,2])
                |- no more
    |- dfs(1, [1,3], [2])
        |- ...
    |- dfs(2, [1,2], [3])
        |- ...
    '''
    
    res = []
    dfs(nums, [], res)
    return res

def dfs(nums, path, res):
    if not nums:
        print ("num: ", nums)
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)



# reference:  https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
def permute2ndMethod(a, l, r):
    if l==r:
        print ("res: " , a)
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]         #swap
            permute2ndMethod(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
            
print (permute([1,2,3]))

a = [1,2,3]
l = len(a)
res = []
permute2ndMethod(a, 0, l-1)

# 2nd  iterative way:
'''
For example, if the input num[] is {1,2,3}: First, add 1 into the initial List<List<Integer>>
(lets call it answer).

Then, 2 can be added in front or after 1. So we have to copy the List<Integer> in answer 
(its just {1}), add 2 in position 0 of {1}, then copy the original {1} again, and add 2
 in position 1. Now we have an answer of {{2,1},{1,2}}. There are 2 lists in the current answer.

Then we have to add 3. first copy {2,1} and {1,2}, add 3 in position 0; then copy {2,1} and {1,2}, 
and add 3 into position 1, then do the same thing for position 3. Finally we have 2*3=6 lists in answer, 
which is what we want.
'''

'''
def permute(self, nums):
    perms = [[]]   
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in xrange(len(perm)+1):   
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n in each position
        perms = new_perms
    return perms


# 3rd if the input has duplicaties like  [1, 1, 2]
 # just avoid inserting a number before any of its duplicates.

def permuteUnique(self, nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            for i in xrange(len(l)+1):
                new_ans.append(l[:i]+s[n]+l[i:])
                if i<len(l) and l[i]==n: break              #handles duplication
        ans = new_ans
    return ans

'''    