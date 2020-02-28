#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 00:41:09 2018

@author: fubao
"""

# leetcode flip game I, II

'''

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip twoconsecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]


'''


def flipGame(s):
    '''
    e.g. string s = "++++" 
    output: all next state by flipping
    '''
    
    #1st 
    # "++++" -> "++--", "--++", "+--+"
    resStr = []
    for i in range(len(s)-1):
        if s[i] == s[i+1] == '+':
            resStr.append(s[:i] + "--" + s[i+2:])
    return resStr


print ("str: ", flipGame("++++"))



'''

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip twoconsecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.

'''

# http://www.cnblogs.com/grandyang/p/5226206.html
#1st recurisve naive method to get all  negative signs "-----....""
def flipGame2(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1] == '+' and not flipGame2(s[:i] + "--" + s[i+2:]):
            return True
    return False

print ("str: ", flipGame2(""))
print ("str: ", flipGame2("+"))
print ("str: ", flipGame2("++"))


'''
time complexity:
T(N) = T(N-2) + T(N-3) + [T(2) + T(N-4)] + [T(3) + T(N-5)] + ... 
        [T(N-5) + T(3)] + [T(N-4) + T(2)] + T(N-3) + T(N-2)
     = 2 * sum(T[i])  (i = 3..N-2)
(N) = 2^(N-1) satisfies the above equation

'''
