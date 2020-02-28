#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:09:18 2018

@author: fubao
"""


#  common backtracking summary

# what's the difference from DFS traversal?

# idea summary:

"""

# give a set, traverse all to the end, and then go back to previous,  similar to DFS?
1st string all permutation
"ABC"      => get 6  permutation


reference:
permute.py  file


2nd:  multiple string to get permutation,  
e.g  "ABC",  "DEF"...,  =>  get 3*3, 9 permutations? "AB", "AD", "AE", "AF",...

reference:  Phone number leetcode 17
"""

# application 1:   Phone number leetcode 17


# application 2:  google 
'''
有很骰子，每个骰子有6个面，上面全是字母，每个骰子用长度为6字符串如"adsads"来表示，
给你一组骰子，和一个target word,问你可不可能用这些骰子投出这个单词。

'''

# use backtracking 
#2nd maybe we can use trie put all permuation of words into trie and search,  redundant?


# 1st backtracking
#   ads ads ; "ads ads", ....,  "ads ads"  6 
  
     
def queryWord(dieWord, target):
    '''
    check the query word
    '''
    
    if not dieWord:
        return []
    
    dieWords = [dieWord] * 3           #die number is 3 here
    
    print ("dieWords: ", dieWords)
    

    def helper(dieWords, currStr, start, ans):
        #termination base case
        if start >= len(dieWords): 
            ans.append(currStr)
            if target == currStr:         #check whether target is in the current result
                return True
            return False
        letter = dieWords[start]        
        for l in letter:
            if helper(dieWords, currStr+l, start+1, ans):
                return True
        return False
    
    ans = []
    queryResult = helper(dieWords, "", 0, ans)
    return ans, queryResult

#  "ab", "ab"

dieWord = "ca"
target = "aa"
print(queryWord(dieWord, target))


dieWord = "ca"
target = "aaa"
print(queryWord(dieWord, target))

























