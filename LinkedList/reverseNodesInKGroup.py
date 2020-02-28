#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 21:46:57 2018

@author: fubao
"""



# 25. Reverse Nodes in k-Group ;     facebook


'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
d
Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''



#first way is to use a stack      O(k) space; o(n) time?
# iterate node until k or None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        '''
        #iterate the linked list k node, if not arriving in the k node
        
        #k=2, 1-2-3-4-5,  dummy->1->2 -3-4;  nextNd = dummy.next (1)
        if head is None:
            return None
        
        stk = []       # stack 
        
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        nextNd = dummy.next
        while(nextNd):
            #push into stack
            i = 0
            while(i < k and nextNd != None):
                stk.append(nextNd)
                nextNd = nextNd.next
                i += 1
            
            if (len(stk) != k): return dummy.next
            while(len(stk)):
                #pop from stack
                current.next = stk.pop(-1)
                print (current.next.val)
                current = current.next
            current.next = nextNd         # important; append the rest nodes
            
            #print ("i: ", i)
        return dummy.next
        '''
    
        #2nd use constant spaces;  1->2->3-4->5; k=2;  prev->1-2  then reverse ;          use singleReverseList to reverse nodes between prev and 2.next 
        
        '''
         0->1->2->3->4->5->6
         |           |   
         pre        next
        
         after calling pre = reverse(pre, next)
         
         0->3->2->1->4->5->6
                  |  |
                  pre next 
        '''
    
        def reverseKNodes(pre, nextNd):
            last = pre.next
            curr = last.next
            while(curr != nextNd):
                last.next = curr.next
                curr.next = pre.next
                pre.next = curr
                curr = last.next
            return last
        
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cnt = 0
        p = head
        while(p):
            cnt += 1
            if cnt % k == 0:
                pre = reverseKNodes(pre, p.next)
                p = pre.next
            else:
                p = p.next
        return dummy.next
    
