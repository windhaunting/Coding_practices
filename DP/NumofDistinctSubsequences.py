#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:42:31 2018

@author: fubao
"""




#  115. Distinct Subsequences
'

'''

 Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

'''


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        '''
        rabbbit
        rabbit
        rabit
        rbt
        
        dp[i][j] 
        
        S:
            r a b b b i t
          1 1 1 1 1 1 1 1      
     T: r 0 1 1 1 1 1 1 1
        a 0 0 1 1 1 1 1 1
        b 0 0 0 1 2 3 3 3
        b 0 0 0 0 1 3 3 3
        
        '''
        
        DP[i+1][j+1] means that S[0..j] contains T[0..i] that many times 
        
        as distinct subsequences. Therefor the result will be mem[T.length()][S.length()].
        
         T[i-1] != S[j-1],              dp[i][j] = dp[i][j-1]  # rabb   rab 
          T[i-1] == S[j-1],        dp[i][j] = dp[i][j-1] + d[i-1][j-1]
         
    From here we can easily fill the whole grid: for each (x, y), we check if S[x] == T[y] we add the previous item and the previous item in the previous row, otherwise we copy the previous item in the same row. The reason is simple:

if the current character in S doesn’t equal to current character T, then we have the same number of distinct subsequences as we had without the new character.
if the current character in S equal to the current character T, then the distinct number of subsequences: the number we had before plus the distinct number of subsequences we had with less longer T and less longer S.
        
#    java code
  public int numDistinct(String S, String T) {
	int sl = S.length();
	int tl = T.length();
	
	int [][] dp = new int[tl+1][sl+1];

	for(int i=0; i<=sl; ++i){
		dp[0][i] = 1;
	}
	
	for(int t=1; t<=tl; ++t){
		
		for(int s=1; s<=sl; ++s){
			if(T.charAt(t-1) != S.charAt(s-1)){
				dp[t][s] = dp[t][s-1];
			}else{
				dp[t][s] = dp[t][s-1] + dp[t-1][s-1];
			}
		}	
	}
	
	return dp[tl][sl];
}
            
            