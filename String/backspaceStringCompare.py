#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 19:35:13 2018

@author: fubao
"""



'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

'''


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        #1st use stack, o(N) time and space 
        
        #2nd traverse backward using two pointers
        LS = len(S)
        LT = len(T)
        # start S's traversing
        i = LS-1;    
        RS = ''     # result for S
        counter = 0
        while (i >= 0):
            if S[i] == '#':
              
                counter += 1
            else:
                if counter != 0:
                    #i -= 1
                    counter -=1
                else:
                    RS = S[i] + RS
            i -= 1
        #print ("RS: ", RS)
        # start T's traversing
        j = LT-1
        RT = ''     # result for T
        counter = 0
        while (j >= 0):
            if T[j] == '#':
                counter += 1
            else:
                if counter != 0:
                    #j -= 1
                    counter -=1
                else:
                    RT = T[j] + RT
            j -= 1
        #print ("RT: ", RT)
        if RS == RT:
            return True
        else:
            return False
                    
                
