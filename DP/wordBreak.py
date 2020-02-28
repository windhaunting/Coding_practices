#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:15:50 2018

@author: fubao
"""




# 139. Word Break


'''
space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        '''
        #1st  DP; one dimension
        leet  leetc    s[i]   previous 0 to i;  
        if le   et :
            j = 2 2:4
            dp[j] s[j:i] in dic:
                so dp[i] true
        '''
        # s = "leet  code",
        #  0 0 0 1  000 1
        #   j = 4 true;    j = 8 true
        #dp is an array that contains booleans

        #dp[i] is True if there is a word in the dictionary that ends at ith index of s 
        # AND  is also True at the beginning of the index i+1 to j; j = 0 to i-1
        
        #complexity worst O(n^3) ;  because s[j:i] worst case o(n)
        
        dp = [False] * (len(s)+1)
        dp[0] = True              # empty space character is set True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[len(s)]
        
        # 2nd use recursive   DFS  java  
        
        '''
        Navigate the given input string.
        Take a blank string and keep adding one character at a time to it.
        Keep checking if the word exist in the dictionary.
        If word exist in the dictionary then add that word to the answer string and make recursive call to the rest of the string.
        If any of the recursive call returns false then backtrack and remove the word from the answer string and again keep adding the characters to string.
        If all the recursive calls return true that means string has been broken successfully.
        See the code for better explanation.
        '''
        
        public class Solution {
        public boolean wordBreak(String s, Set<String> dict) {
            // DFS
            Set<Integer> set = new HashSet<Integer>();
            return dfs(s, 0, dict, set);
        }
        
        private boolean dfs(String s, int index, Set<String> dict, Set<Integer> set){
            // base case
            if(index == s.length()) return true;
            // check memory
            if(set.contains(index)) return false;
            // recursion
            for(int i = index+1;i <= s.length();i++){
                String t = s.substring(index, i);          //from index  to index+1, index+2
                if(dict.contains(t))
                    if(dfs(s, i, dict, set))
                        return true;
                    else
                        set.add(i);
            }
            set.add(index);
            return false;
        }
    }
            
        