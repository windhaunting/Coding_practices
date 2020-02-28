#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 01:07:32 2018

@author: fubao
"""



#         https://people.cs.clemson.edu/~bcdean/dp_practice/

1) Overlapping Subproblems
2) Optimal Substructure

Steps:
    
1.define problem solution representation
2. find transit function
3. initialization
4. memoization / tabulation

 #     Dynamic programming examples:
 
1.  Longest Increasing Subsequence

The Longest Increasing Subsequence (LIS) problem is to find the length of the longest
subsequence of a given sequence such that all elements of the subsequence are sorted
in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is
6 and LIS is {10, 22, 33, 50, 60, 80}.

Then, L(i) can be recursively written as:
L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists.

2.  Longest Common Subsequence
Given two sequences, find the length of longest subsequence present in both of them. A
subsequence is a sequence that appears in the same relative order, but not
necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are
subsequences of “abcdefg”. So a string of length n has 2^n different possible
subsequences.

If last characters of both sequences match (or X[m-1] == Y[n-1]) then
L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])
If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then
L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2])
    

1. Maximum Value Contiguous Subsequence. 
 
2. Making Change. 
 
3. Longest Increasing Subsequence. 