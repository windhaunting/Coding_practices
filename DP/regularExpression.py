#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:39:25 2018

@author: fubao
"""

# 10. Regular Expression Matching

# facebook

'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

'''

a  a
a  *a
ba  ba

ba  *a
cba *


          s
        p       a  b  *
             1  0  0  0
           a 0  1  0  1
           b 0  
           b 0
       
   if s[i] == p[j] or p[j] = '.'
   
dp[i][j]   dp[i-1][j-1]              
overlapping subproblem        ad, cd         ade, cde

a*    ==>  '' or 'a', 'aa','aaa',...
dp[i][j]  indicate  s[i] and p[i] matches?

aaa vs aaa


dp[i+1] = dp[i] and s[i+1] = p[j+1] or p[j+1] == '.' or '*'  xx

a* matching means  "" or "a" or "aa" or more 'a"

simply
define the transistion; initialize
dp[i][j]  indicate whether the substring from 0 to ith characters in s 
                      matches with substring from 0 to jth character in p
the range of i j:
    dp[len(s)+1][len(p)+1] ?
    
    initialize: dp[0][0]  = true   # fetch 0 and 0 from p and s respectively
    
dp[i][j] = 

(1)  if p[j] != '*' : 
    dp[i-1][j-1]  if s[i] == p[j] or p[j] == '.'

(2)  if p[j] = '*' :
     dp[i][j-2]           ( e.g. a vs ab*, i = 1, j = 3 for * )
   or dp[i-1][j]  if s[i] == p[j-1] or p[j-1] == '.'          # cab vs cab*     cab vs c.*

(3)otherwise False

a, a
aa,  ab  
aa   a*
aa   a.
a  a.*


one corner case
s is empty;  p is a* also match

'''


# reference https://www.youtube.com/watch?v=l3hda49XcDE
import unittest


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #1st use DP
        m, n = len(s) + 1, len(p) + 1
        matches = [[False] * n  for _ in range(m)]

        # Match empty string with empty pattern
        matches[0][0] = True

        # Match empty string with .*
        for i, element in enumerate(p[1:], 2):
            matches[0][i] = matches[0][i - 2] and element == '*'

        for i, ss in enumerate(s, 1):
            for j, pp in enumerate(p, 1):
                if pp != '*':
                    # The previous character has matched and the current one
                    # has to be matched. Two possible matches: the same or .
                    matches[i][j] = matches[i - 1][j - 1] and (ss == pp or pp == '.')
                else:
                    # Horizontal look up [j - 2].
                    # Not use the character before *.
                    matches[i][j] |= matches[i][j - 2]

                    # Vertical look up [i - 1].
                    # Use at least one character before *.
                    #   p a b *
                    # s 1 0 0 0
                    # a 0 1 0 1
                    # b 0 0 1 1
                    # b 0 0 0 ?
                    if ss == p[j - 2] or p[j - 2] == '.':
                        matches[i][j] |= matches[i - 1][j]

        return matches[-1][-1]
        
      # optimized the space for the first version
      #  Instead of storing it within a table, it could just use an array:
        def isMatchOptimizedSpace(self, s, p):
            prev = [False, True]
            for j in range(len(p)):
                prev.append(p[j]=='*' and prev[j])
    
            for i in range(len(s)):
                curr = [False, False]
                for j in range(len(p)):
                    if p[j]=='*':
                        curr.append(curr[j] or curr[j+1] or (prev[j+2] and p[j-1] in (s[i], '.')))
                    else:
                        curr.append(prev[j+1] and p[j] in (s[i], '.'))
                prev = curr
            return prev[-1]
    
    
    
    # 2nd using recursive way
    '''
     若p为空，若s也为空，返回true，反之返回false

    - 若p的长度为1，若s长度也为1，且相同或是p为'.'则返回true，反之返回false
    
    - 若p的第二个字符不为*，若此时s为空返回false，否则判断首字符是否匹配，且从各自的第二个字符开始调用递归函数匹配
    
    - 若p的第二个字符为*，若s不为空且字符匹配，调用递归函数匹配s和去掉前两个字符的p，若匹配返回true，否则s去掉首字母
    
    - 返回调用递归函数匹配s和去掉前两个字符的p的结果
    '''    
    cache = {}
    def isMatch(self, s, p):
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not p:
            return not s
        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
                self.cache[(s, p)] = True
                return True
        if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True
        self.cache[(s, p)] = False
        return False

        
class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(Solution().isMatch(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "abb"
        self.assertFalse(Solution().isMatch(s, p))

    def test_symbol_0(self):
        s = ""
        p = "a*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))


if __name__ == "__main__":
    unittest.main()