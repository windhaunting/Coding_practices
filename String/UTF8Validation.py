#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:00:31 2019

@author: fubao
"""

# facebook
# UTF8-Validation

'''
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
'''


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        #idea 1 here use string operation establish a mapping between a binary to 1-byte, n-byte 
        #first transfer each data into binary, then figure out its one byte or n byte, then judge how many next should be used
        #define a function to figure out whether a binary is 1-byte or n byte


        # transfer to binary
        if data is None or len(data) == 0:
            return False

        next_ind = 0
        for i in range(0, len(data)):
            bstr = bin(data[i])[2:].zfill(8)
            
            #print ("bstr: ", bstr)
            if next_ind > 0:
                if bstr[0:2] != '10':
                    return False
                next_ind -= 1
                continue

            #get its 1-byte, n-byte or none
            byte = self.isByte(bstr)
            if byte is None:
                return False

            if byte == 2:
                next_ind = 1
            elif byte == 3:
                next_ind = 2
            elif byte == 4:
                next_ind = 3
        
        if next_ind > 0:
            return False
        else:
            return True
    
    def isByte(self, bstr):
        if bstr[0] == '0':
            return 1
        elif bstr[0:3] == '110':
            return 2
        elif bstr[0:4] == '1110':
            return 3
        elif bstr[0:5] == '11110':
            return 4
        return None
    
    
    #2nd idea use bit reference:  https://leetcode.com/problems/utf-8-validation/solution/
        