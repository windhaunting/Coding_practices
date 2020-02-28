#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:36:43 2018

@author: fubao
"""



# 76. Minimum Window Substring
# Smallest Substring of All Characters

# facebook

'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

'''

#https://leetcode.com/problems/minimum-window-substring/discuss/26804

import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        '''
        #1st  naive way fail for time limit:   generate all possible substring O( n* (m*n^2))  complexity  
        dic = defaultdict()
        for a in t:
            dic[a] = 1
        print (dic)
        minStr = ""
        minLen = 2**32
        
        i = len(dic)
        strLen = len(s)
        while (i <= strLen):
          for j in range(strLen):
              tmpStr = s[i:j+len(dic)]
              flag = True
              for t in tmpStr:
                  if t not in dic:
                      flag = False
                      break
              if flag:
                if len(tmpStr) < minLen:
                    minLen = len(tmpStr)
                    minStr = tmpStr
          i += 1
        return minStr
        '''
    
        # 2nd :
        '''
           At each iteration, we examine a temporary substring [str.charAt(headIndex),
           str.charAt(headIndex+1),..., str.charAt(tailIndex)] and keep a copy of 
           the shortest valid substring we’ve seen so far. Said differently, 
           we keep incrementing tailIndex until the above substring contains every unique character in arr.
    
          If the size of the resulting substring equals to arr.length 
          then we return it since by definition there can’t be a shorter
          valid substring (otherwise, it’ll be missing 1 or more unique characters from arr).
    
          Once we found a valid substring, we increment headIndex as long the
          substring remains valid. At every increment we also check if the current
          valid substring is shorter than the previously kept one. If it is, 
          we update result to be the current substring.

        '''
        #The current window is s[i:j] and the result window is s[I:J]. 
        #In need[c] I store how many times I need character c (can be negative) 
        #and missing tells how many characters are still missing. 
        #In the loop, first add the new character to the window. 
        #Then, if nothing is missing,  remove as much as possible from the window start 
        #and then update the result.

        '''
        need = collections.Counter(t)  # t's hashmap
        missing = len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):         # Start from index 1 not 0 
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
        '''
        '''
        S = "ADOBECODEBANC"
        T = "ABC"
        Minimum window is "BANC".
        '''
        
        dic = collections.defaultdict(str)
        for a in t:
            dic[a] = 1
        print (dic)
        targetLen = len(dic)
        i = 0
        start = 0
        end = 0
        for j, c in enumerate(s, 1):
            if dic[c] > 0:
                targetLen -= dic[c]   #
            dic[c] -= 1
            if targetLen == 0:
                while(i < j and dic[s[i]] < 0):
                    dic[s[i]] += 1
                    i += 1
                if end == 0 or j-i < end-start:
                    start = i
                    end = j
        print (s[start:end])
        return s[start:end]

        
        '''
            # my implementation, SUCCESS which is too trivial
    
            targetHash = {}
            
            for c in t:
                if c not in targetHash:
                    targetHash[c] = 1
                else:
                    targetHash[c] += 1
            
            
            srcHash = {}
            
            count = 0         #decide when T matched in S
            left = 0
            right = 0
            minWindLen = 2**32
            minStart = 0
            
            #print ("target hash: ", targetHash)
            while (right < len(s)):
                
                if s[right] in targetHash and targetHash[s[right]] > 0:
                    if s[right] not in srcHash:
                        srcHash[s[right]] = 1
                    else:
                         srcHash[s[right]] += 1
                    if (srcHash[s[right]] <= targetHash[s[right]]):
                        count += 1
                
                if count == len(t):
                        
                    
                    while (s[left] not in targetHash  or (s[left] in srcHash and s[left] in targetHash and srcHash[s[left]] > targetHash[s[left]])):
                        if s[left] in targetHash:
                            srcHash[s[left]] -= 1
                        left += 1
                        
                    if minWindLen > (right-left+1):
                        minWindLen = right-left+1
                        minStart = left
                                    
                
                right += 1
                    
            
            return s[minStart: minStart+minWindLen] if minWindLen <= len(s) else ""
        
         '''
        

SolutionObj = Solution()
s = "ADOBECODEBANC"
t = "ABC" 
SolutionObj.minWindow(s, t)

    