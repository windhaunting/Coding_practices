#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:47:17 2018

@author: fubao
"""

# 21. Merge Two Sorted Lists

# 

'''
Merge list
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        #1st  compare and merge iterative
        h1 = l1
        h2 = l2
        h = ListNode(-1)
        p = h
        while(h1 and h2):
            if h1.val < h2.val:
                h.next = h1 # ListNode(h1.val)
                h = h.next
                h1 = h1.next
            else:
                h.next  = h2 # ListNode(h2.val)
                h = h.next
                h2 = h2.next
        if h2 is not None:
            h.next = h2
            
        if h1 is not None:
            h.next = h1
        return p.next
    
    
    #2nd method recursive    T(n) = 1 + T(n-1) ;  O(n);        if it's array merging; T(n) = n + T(n-1) = > O(n^2)
    def mergeTwoListsRecursive(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    