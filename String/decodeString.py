#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:01:30 2018

@author: fubao
"""

# 394. Decode String


'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


'''





class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        #1st using stack stack num and curr when counter '[' and pop out when counter ']'
        
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
    


'''    
2nd using recursive version;   c ++ 


class Solution {
public:
    string decodeString(string s) {
        int pos = 0;
        return helper(pos, s);
    }
    
    string helper(int& pos, string s) {
        int num=0;
        string word = "";
        for(;pos<s.size(); pos++) {
            char cur = s[pos];
            if(cur == '[') {
                string curStr = helper(++pos, s);
                for(;num>0;num--) word += curStr;
            } else if (cur >= '0' && cur <='9') {
                num = num*10 + cur - '0';
            } else if (cur == ']') {
                return word;
            } else {    // Normal characters
                word += cur;
            }
        }
        return word;
    }
};
            '''
            
            
            
            
# 2nd time to practice
            
            
class Solution:
    def decodeString(self, s: str) -> str:
        #idea 1. iteratively traverse the string and put each character into a stack, 
        # until we encounter a right bracket, then use the following way to pop from stack and process it,
        # then decide when to continue traversing until the end
        # then decide
        
        if s is None or len(s) == 0 or s == '':
            return ''
        
        stk = []
        
        res = ''
        subStr = ''
        for c in s:
            if c != ']':
                # push into stack
                stk.append(c)
            else:
                # process stack
                #print ("stk", stk)
                while('[' != stk[-1]):
                    tmp = stk.pop()
                    subStr = tmp + subStr
                
                stk.pop()   # pop '['
                #print ("digit", digit, subStr)
                digit = ''
                while (len(stk) != 0 and stk[-1].isdigit()):
                    digit = stk.pop() + digit
                digit = int(digit)
                subStr = self.copyStr(subStr, digit)
                #print ("subStr", subStr)
                
                if len(stk) == 0:
                    res += subStr
                    subStr = ''
                stk.append(subStr)        # need to add to add to stack for case e.g. "3[a]2[b4[F]c]" 
                subStr = ''
        res += "".join(stk)
        return res
                
    def copyStr(self, st, m):
        i = 1
        tmp = st
        while (i < m):
            st += tmp
            i += 1
        return st
    