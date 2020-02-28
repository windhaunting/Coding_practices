#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 18:23:46 2018

@author: fubao
"""


#  80. Decoded String at Index



'''
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

 

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".
Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
 

Note:

2 <= S.length <= 100
S will only contain lowercase letters and digits 2 through 9.
S starts with a letter.
1 <= K <= 10^9
The decoded string is guaranteed to have less than 2^63 letters.

'''

import re

class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        '''
        # really memory limit problem one naive way is to iterate the string S. Use a list to maintain its current substring cur; when it's a character in 'a-z' or 'A-Z'
        # when it's a digit d in '2-9'; copy the cur 'd-1' times;   otherwise skip;
        # time complexity is high;  letter has number of A, digits has number of B; the worst complexity is A*B ?
        #or memory limit problem   e.g. "a2345678999999999999999"   1
        
        curLst = []
        reg = re.compile('[a-z]')
        for i in range(0, len(S)):
            if reg.search(S[i]):
                curLst.append(S[i])
            else:          # because the question said S only contain 'a-z' and S
                digit = int(S[i])
                curLst = curLst*digit
        return curLst[K-1]
        '''
        
        '''
        # 2nd this problem only consider the K-1 string, so we terminate it early when there are K characters inside the curLst
        # also has memory limit problem  e.g. "y959q969u3hb22odq595"    222280369
        curLst = []
        reg = re.compile('[a-z]')
        for i in range(0, len(S)):
            if reg.search(S[i]):
                curLst.append(S[i])
            else:          # because the question said S only contain 'a-z' and S
                digit = int(S[i])
                curLst = curLst*digit
            if len(curLst) >= K:
                return curLst[K-1]
            
        return curLst[K-1]
        '''
        
        # a trick is that K% size is the same as K  ;  considering the repetition
        #leet2code3
        # leet leet code leet leet code leet leet code; K = 10; K = 22 is the same? 22%12
        # time complexity O(len(S)); O(1) 
        
        length = 0
        for c in S:
            if c.isdigit():
                length *= int(c)
            else:
                length += 1
        
        for c in reversed(S):
            # if c.isdigit():
            K %= length
                
            if K == 0 and c.isalpha():
                return c
                
            if c.isdigit():
                length /= int(c)
            else:
                length -= 1
            
        
        
