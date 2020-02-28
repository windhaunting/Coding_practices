#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:06:05 2018

@author: fubao
"""



#  211. word dictionary Add and Search Word - Data structure design


'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

'''

#1st solution not to use trie ;  use hashmap store key: len(words) ,value: words list

#2nd use trie

import collections
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            self.word_dict[len(word)].append(word)
            

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        
        if '.' not in word:
            return word in self.word_dict[len(word)]

        for w in self.word_dict[len(word)]:
            success = True
            for index, ch in enumerate(word):
                if ch != w[index] and ch != '.':
                    success = False
                    break

            if success:
                return True
        return False



#2nd use trie
  
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)  #key is character, value is TireNode
        self.isWord = False
    
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):    #recursive search
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:        #search word done
            if node.isWord:
                self.res = True
            return 
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])  #  #[word[0]] TLE NOT EFFICIENT?
            #if word[0] not exist, return 
            if not node:
                return 
            self.dfs(node, word[1:])