#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:55:04 2018

@author: fubao
"""


# 208. Implement Trie (Prefix Tree)



#  https://leetcode.com/problems/implement-trie-prefix-tree/solution/

# http://www.cnblogs.com/grandyang/p/4491665.html


'''

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

'''

#字典树 

class TreeNode:
    def __init__(self):
        self.children = [None]*26       # 26 letters here
        
        self.endFlag  = False        # end of world flag
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nd = TreeNode()
    
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        #word = lower(word)    # default lowercase
        p = self.nd
        for i, w in enumerate(word):
            #print ("ord(w)-97: ", ord(w)-97)
            if p.children[ord(w)-ord('a')] is None:
                p.children[ord(w)-ord('a')] = TreeNode()
            
            p = p.children[ord(w)-ord('a')]    
        
        p.endFlag = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.nd
        for i, w in enumerate(word):
            if p.children[ord(w)-ord('a')] is None:
                return False
            
            p = p.children[ord(w)-ord('a')]     
    
        if p is not None and p.endFlag == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.nd
        for i, w in enumerate(prefix):
            if p.children[ord(w)-ord('a')] is None:
                return False     
            p = p.children[ord(w)-ord('a')]     

        if p is not None:
            return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
        