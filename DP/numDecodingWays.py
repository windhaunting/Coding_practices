#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:40:04 2018

@author: fubao
"""


#  91. Decode Ways



'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.


'''

#reference: http://bangbingsyb.blogspot.com/2014/11/leetcode-decode-ways.html

'''
#1st  use DP             2nd use DFS
思路：
假设解码函数为h。对于一位数X，只能解码成h[X]。而对于一个两位数XY：
1. 如果XY<=26，那么能解码成h[X]h[Y];   h[XY]
2. 否则，只能解码成h[X]h[Y]
由于只要求计算最多的解码方法而并不要求每种解码的结果，所以用DP做更为合适高效。

定义dp[i+1]为能解码长度为i+1的string s[0:i]的方法数：
1. dp[0] = 1，dp[1] = 0
2. v = s[i-1]*10+s[i]：
v<=26： dp[i+1] = dp[i] + dp[i-1]
v>26：dp[i+1] = dp[i]

corner case：有0的情况
Y = 0：显然无法解码成h[Y]，此时只能看h[XY]是否valid：dp[i+1] = dp[i-1]
X = 0：显然无法解码成h[XY]，此时dp[i+1] = dp[i]

整理总结corner case：
XY可以解码的条件是：9<XY<=26
Y可以单独解码的条件是：Y != '0'

'''


'''

            "1   2   3     4    5"
s index:     0   1   2     3    4
dp index  0  1   2   3     4    5
dp value  1  1   2   3     3    3

 #dp[i] means the number of decoding way for string s[0:i] not including i
 dp[0] = 1
 dp[1]  = 0   not 1,   why?  s[0:1]
 
s[i-1]s[i] <= 26
consider dp[i+1] + dp[i-2]   
also dp[i+1] += dp[i-1]      if s[i] is separately decoded with s[i-1]

if s[i-1]s[i] > 26: only one way
dp[i+1] = dp[i]

'''
def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    
    if s is None or len(s) == 0:
        return 0
    dp = [0] * (len(s) + 1)      #dp[i+1] means the number of decoding way for string s[0:i+1]
    dp[0] = 1
    #dp[1] = 1                  # consider if s[0] = '0', we cant not decode.   , also we update dp[1] later
    
    for i in range(1, len(s)+1):
        if int(s[i-1]) != 0:
            dp[i] += dp[i-1]
        if i-2 >= 0 and 9 < int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    return dp[len(s)]


s = "12345"
print (numDecodings(s))



#2nd use DFS
'''
首先考虑：一位数字可以表示一个字母，比如1-A，两位字符也可以表示一个字母比如26-Z。那么根据是1个或者2个字符表示1个字母很快可以想到一个DFS的思路。

      对于每个大于2个字符的字符串S[n]，我们可以把它分解成两种情况：

     1. 前面n-2个字符的子串 和 最后两个字符的子串。

    2. 前面n-1个字符的子串 和 最后一个字符的子串。

    如果用nums()表示A-Z字符串可以匹配的个数，我们可以得到 

nums(S[1..n]) = nums(S[1...n-2] ) * nums(S[n-1，n])  +  nums(S[1...n-1] ) * nums(S[n]) .

    DFS 终止条件为：当要找的字符串长度小于3的时候，我们通过单独的分析一一列举出来。

'''


'''
639. Decode Ways II
DescriptionHintsSubmissionsDiscussSolution

A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:

Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".

Example 2:

Input: "1*"
Output: 9 + 9 = 18

Note:

    The length of the input string will fit in range [1, 105].
    The input string will only contain the character '*' and digits '0' - '9'.

'''



            "1   *  3"
s index:     0   1   2
dp index  0  1   2   3
dp value  1  1
dp[i] = dp[i]

127

12*
1*2
1*7     (>7)

*11

1**    

**1 or ***

s[i-2] = '*' or '1-9' or '0'

how many ways of decoding for **     => 9*9 + 26-9

if * not in s[i-2:i]:
    if int(s[i-1]) != 0:
            dp[i] += dp[i-1]
        if i-2 >= 0 and 9 < int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
else:
    
    if s[i-2] != 0 and s[i-2] == '*' and s[i-1] != '*':      # *11
    
        if int(s[i-1]) != 0:
            dp[i] += dp[i-1]
        if i-2 >= 0 and 9 < int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
            
    elif s[i-1] == '*' and s[i-2] != '*':      # 1*2       1**
    
       if s[i] != '*' and int(s[i]) < 7:         # 1*2
           
            dp[i] += 2*dp[i-2]
       elif s[i] != '*' and int(s[i]) >= 7: 
            dp[i] += 1*dp[i-2]
       elif s[i] == '*':        # 1**   
           dp[i] == (9*9+26-9)*dp[i-2]
           
       dp[i] = 9*dp[i-1]
        
        if s[i-2]    
        
    elif s[i-1] == '*' and s[i-2] == '*':         #**1,  **7 or ***
        
'''

        
# reference:
        
   # http://blog.csdn.net/juzihongle1/article/details/74992380
   # http://www.cnblogs.com/grandyang/p/7279152.html