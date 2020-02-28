#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:54:58 2018

@author: fubao
"""

# programming summary




#### Trie  


# fast for lookup of words in a dictionary;  
# what's the advantage compared to the normal hashmap? average time o(l) words length; space is smaller than regular hash



# implementation


# how to store the children node;  use list of list; dictionary of dictionaries to represent trie
# or use a dictionary to present trie children (edge connection)


# reference https://www.youtube.com/watch?v=AXjmTQ8LEoI


from collections import defaultdict

class TrieNode(object):
    def __init__ (self, endOfWord = False):
        #self.char = char               # store the charcter when endofWord is
        self.endofWord = endOfWord
        self.children = defaultdict(TrieNode)           #key is character, value is another TrieNode it points to
        self.prefixCount = 0          #how many prefix in the trie words


class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    
    def insert(self, word):
        '''
        insert word into trie
        '''
        current = self.root
        
        for c in word:         # check every character
            if c not in current.children:
                current.children[c] = TrieNode(False)      #add 
                
            current = current.children[c]
            current.prefixCount += 1
        current.endofWord = True
        

    def search(self, word):                # search whole word, not prefix
        current  = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.endofWord
    
    def remove(self, word):
        '''
        not real delete, make endofword flag as false
        '''
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            if current.endofWord:
                current.endofWord = False
            current = current.children[c]
        current.endofWord = False
        return True
     
    def countPrefix(self, word):
        '''
        how many words have this input words as prefix
        '''
        current = self.root
        for c in word:
            if c not in current.children:
                return 0
            current = current.children[c]
        return current.prefixCount
    
    def searchPrefixWord(self, root, prefix ):
        '''
        auto fill the rest of words
        '''
        out = []
        if root.endofWord:
            out.append( prefix )
		
        for ch in root.children:
            if isinstance( prefix, tuple ):
                self.searchPrefixWord( root.children[ch], prefix + (ch,) )
            elif isinstance( prefix, list ):
                tmp = self.searchPrefixWord( root.children[ch], prefix + [ch] )
            else:
                tmp = self.searchPrefixWord( root.children[ch], prefix + ch )
            out.extend(tmp)
        return out
    
    def enumerateAllWordWithPrefix(self, prefixs):
        '''
        search all words with common prefix
        '''
        current = self.root
        for c in prefixs:
            if c not in current.children:
                return []
            current = current.children[c]
        return self.searchPrefixWord(current, prefixs)

TrieObj = Trie()

TrieObj.insert('abcd')
TrieObj.insert('abcef')
TrieObj.insert('adef')

print (TrieObj.search('abcd'))
print (TrieObj.search('abc'))
print (TrieObj.search('abcdef'))
print (TrieObj.search('abcef'))
print (TrieObj.search('adef'))

TrieObj.remove('abcd')
print (TrieObj.search('abcd'))

TrieObj.insert('abcd')
print (TrieObj.search('abcd'))

TrieObj.insert('abgef')
print (TrieObj.enumerateAllWordWithPrefix("ab"))




# another simple way to create Trie.,
class Trie:
    def __init__(self):
        # letter -> next trie node.
        self.paths = defaultdict(Trie)
        # If a word ends at this node, then this will be a positive value
        # that indicates the location of the word in the input list.
        self.wordEndIndex = -1

    # Adds a word to the trie - the word will be added in 
    # reverse (e.g. adding abcd adds the path d,c,b,a,$index) to the trie.
    # word - string the word to be added
    # index - int index of the word in the list, used as word identifier.
    def addWord(self, word, index):
        trie = self
        for j, char in enumerate(word): 
            trie = trie.paths[char]
        trie.wordEndIndex = index         # word ending flag use the the words list's index
 
def makeTrie(words):
    trie = Trie()
    for i, word in enumerate(words):
        trie.addWord(word, i)
    return trie

