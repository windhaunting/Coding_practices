#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 01:00:12 2019

@author: fubao
"""

# backtracking combinations

'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''


res_lst = []
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # idea  use backtracking.  if n = 4, k =2 , we select 1,2,3,4 each tree branch, then the next brach select the rest 3 number  like the permutation of An(k) = time complexity
    
            
        def helper(n, k, pos, cur_lst):
            
            if len(cur_lst) == k:
                global res_lst
                res_lst.append(cur_lst)
                return            
            
            for i in range(pos, n+1):
                helper(n, k, i+1, cur_lst + [i])
            
        pos = 1
        cur_lst = []
        global res_lst
        res_lst.clear()
        helper(n, k, pos, cur_lst)
        #print ("res_lsttt", res_lst)
        
        return res_lst

    