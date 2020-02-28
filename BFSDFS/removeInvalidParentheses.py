#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:08:58 2018

@author: fubao
"""


#  301. Remove Invalid Parentheses

#facebook

'''

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]


'''


#use dfs idea recursively
#1. check left and right parenthesis,
# if r !=0 || l !=0 need to decide delete the parenthesis or not

# delete parenthesis recursively

# reference:  http://www.cnblogs.com/grandyang/p/4944875.html
        
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        #1st  USE DFS recursive
        #reference:   http://zxi.mytechroad.com/blog/string/leetcode-301-remove-invalid-parentheses/
        #check whether a input string is valid
        #copmpute min number of '(' and ')' to remove unbalanced ')' + unbalanced '('
        # try all possible ways to remove right ')'s and left '('s. Remove ')' first to make prefix valid
        
        l = 0   # left extra parenthesis counter
        r = 0   # right extra parenthesis counter
        
        for c in s:
            if c == '(':
                l += 1
            if c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
                    
        start = 0
        ans = []
        print ("l, r : ", l, r, s)
        self.dfsHelper(s, start, l, r, ans)
        return ans
    
    
    # check a string is a valid parenthesis string 
    def isValid(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            if c == ')':
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

        
        
    def dfsHelper(self, s, start, l, r, ans):
        #termination. Nothing to remove.

        if l == 0 and r == 0:
            print ("l, r here: ", l, r, s)
            if self.isValid(s):
                print ("l, r ddd: ", l, r,s)

                ans.append(s)
                return
        
        for i in range(start, len(s)):
            # We only remove the first parenthes 
            #if there are consecutive ones to avoid duplications.
            if (i != start and s[i] == s[i-1]):
                continue
            if (s[i] == '(' or s[i] == ')'):
                #curr = s
                curr= s[0:i] + s[i+1:len(s)]
                #print ("l, r ttttt: ", l, r,s, curr)
                if (r > 0 and s[i] == ')'):                    #  remove ')'
                    self.dfsHelper(curr, i, l, r-1, ans)
                elif ((l > 0) and s[i] == '('):
                    self.dfsHelper(curr, i, l-1, r, ans)
        
    #2nd use BFS
    #reference:  http://www.cnblogs.com/yrbbest/p/5049891.html
    '''
    方法是我们每次去掉一个"("或者")"，然后把新的string加入到Queue里，
    继续进行计算。要注意的是需要设置一个boolean foundResult，
    假如在这一层找到结果的话，我们就不再继续进行下面的for循环了。
    这里应该还可以继续剪枝一下，比如记录当前这个结果的长度len，
    当queue里剩下的string长度比这个len小的话，我们不进行验证isValid这一步。
    '''
    