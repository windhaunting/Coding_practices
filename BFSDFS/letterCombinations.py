#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:10:29 2018

@author: fubao
"""



# 17. Letter Combinations of a Phone Number
  
# facebook


'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''

#it's like dfs traversing;
#we can use recursive or iterative way


# reference : https://www.youtube.com/watch?v=fLy8t33M1qQ

#234;     a    b         c
        d e f d e f    d e f
      
     
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if len(digits) == 0:
        return []
    def helper(digits, currStr, start, ans):
        #termination
        if start >= len(digits): 
            ans.append(currStr)
            return 
        
        #get letter
        letters = mapDic[int(digits[start])]
        for l in letters:
            helper(digits, currStr+l, start+1, ans)
            
    mapDic = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    
    ans = []
    helper(digits, "", 0, ans)
    return ans

#digits = "234"
#print ("ans1: ", letterCombinations(digits))


#iterative way      similar to BFS
def letterCombinationsIterate(digits):
    #caretsian
    # "" = > a, b, c  => ab, ad, ae, 
    
    if len(digits) == 0:
        return []
    
    ans = [""]
    mapDic = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    for i in range(0, len(digits)):
        d = int(digits[i])
        while ( len(ans[0]) == i):
            t = ans.pop(0)
            ans += [ t + c for c in mapDic[d]]
    return ans

digits = "234"
print ("ans1: ", letterCombinationsIterate(digits))
