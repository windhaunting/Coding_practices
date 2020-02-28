#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:24:32 2020

@author: fubao
"""

substring match

pattern search



1st: KMP

 The time complexity of KMP algorithm is O(m+n) in the worst case. 
 
 
 http://bangbingsyb.blogspot.com/2014/11/leetcode-implement-strstr-kmp.html
https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/


2nd rabin-karp-algorithm

https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/


The average and best case running time of the Rabin-Karp algorithm is O(n+m), 
but its worst-case time is O(nm). Worst case of Rabin-Karp algorithm occurs
 when all characters of pattern and text are same as the hash values of all 
 the substrings of txt[] match with hash value of pat[]. For example pat[] = “AAA” and txt[] = “AAAAAAA”
