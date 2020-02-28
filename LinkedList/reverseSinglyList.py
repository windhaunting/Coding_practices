#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 00:03:45 2018

@author: fubao
"""

# 206. Reverse Linked List  print a single linked list reversely

'''
Reverse a singly linked list.

click to show more hints.

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #1st iterative way
        '''
        if head is None or head.next is None:
            return head
        p1 = head
        p2 = p1.next
        
        head.next = None;
        while(p1 is not None and p2 is not None):
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
 
        return p1
        '''    
            
        # 2nd recursive way:
        if head is None or head.next is None:
            return head
        p1 = head.next
        head.next = None
        p2 = self.reverseList(p1)
        p1.next = head         
        return p2
        
    
    