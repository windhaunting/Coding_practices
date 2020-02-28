#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 18:03:45 2018

@author: fubao
"""

# one-edit-distance

'''

Given two strings S and T, determine if they are both one edit distance apart.


'''

'''

3 operations:
    
 add
 delete
 change 
'''

'''
1. 两个字符串的长度之差大于1，那么直接返回False

2. 两个字符串的长度之差等于1，那么长的那个字符串去掉一个字符，剩下的应该和短的字符串相同 (或者短字符 加个字符和长的应该相同)

3. 两个字符串的长度之差等于0，那么两个字符串对应位置的字符只能有一处不同。
'''
 
def isOneEditDistance(s, t):
    if s == t:
        return False
    l1, l2 = len(s), len(t)
    if l1 > l2: # force s no longer than t
        return isOneEditDistance(t, s)
    if l2 - l1 > 1:               # length difference bigger than 2 return false
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            if l1 == l2:
                s = s[:i]+t[i]+s[i+1:]  # replacement
            else:
                s = s[:i]+t[i]+s[i:]  # insertion
            break                    #only once judgement
    return s == t or s == t[:-1]

print (isOneEditDistance('ABD', 'CBD'))