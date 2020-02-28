#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:41:58 2018

@author: fubao
"""


#  336. Palindrome Pairs



'''

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]



'''






# naive method   TLE



# 2nd use hashmap set

# 
'''
需要一个set来保存出现过的单词的长度，算法的思想是，遍历单词集，

对于遍历到的单词，我们对其翻转一下，然后在哈希表查找翻转后的字符串是否存在，注意不能和原字符串的坐标位置相同，因为有可能一个单词翻转后和原单词相等，现在我们只是处理了bat和tab的情况，还存在abcd和cba，dcb和abcd这些情况需要考虑，这就是我们为啥需要用set，由于set是自动排序的，我们可以找到当前单词长度在set中的iterator，然后从开头开始遍历set，遍历比当前单词小的长度，
比如abcdd翻转后为ddcba，我们发现set中有长度为3的单词，然后我们dd是否为回文串

'''


 def is_palindrome(check):
        return check == check[::-1]

    words = {word: i for i, word in enumerate(words)}
    valid_pals = []
    for word, k in words.iteritems():
        n = len(word)
        for j in range(n+1):       #for each word string's substring check Palindrome
            pref = word[:j]
            suf = word[j:]
            if is_palindrome(pref):
                back = suf[::-1]
                if back != word and back in words:
                    valid_pals.append([words[back],  k])
            if j != n and is_palindrome(suf):
                back = pref[::-1]
                if back != word and back in words:
                    valid_pals.append([k, words[back]])
    return valid_pals

