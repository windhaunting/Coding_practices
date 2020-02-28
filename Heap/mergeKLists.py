#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:31:20 2018

@author: fubao
"""

#  Merge K Sorted lists Arrays

#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# facebook

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# reference:          https://leetcode.com/problems/merge-k-sorted-lists/solution/
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        
        #1st  Approach #1 Brute Force [Accepted]
        '''
        Traverse all the linked lists and collect the values of the nodes into an array.
        Sort and iterate over this array to get the proper value of nodes.
        Create a new sorted linked list and extend it with the new nodes.
        '''
       # Time complexity : O(NlogN) where N is the total number of nodes.
       
       
       #2nd Approach #2 Compare one by one [Accepted]
       '''
       Compare every k nodes (head of every linked list) and get the node with the smallest value.
       Extend the final sorted linked list with the selected nodes
       '''
       
       # 3rd
       #Approach #3 Optimize Approach 2 by Priority Queue [Accepted]
       #Almost the same as the one above 
       #but optimize the comparison process by priority queue. 
       # Time complexity : O(Nlogk) where \text{k}k is the number of linked lists.
       # Space complexity : O(n) Creating a new linked list costs O(n) space.
      from Queue import PriorityQueue

        def mergeKLists(self, lists):
            """
            :type lists: List[ListNode]
            :rtype: ListNode
            """
            head = point = ListNode(0)
            q = PriorityQueue()
            for l in lists:
                if l:
                    q.put((l.val, l))
            while not q.empty():
                val, node = q.get()
                point.next = ListNode(val)
                point = point.next
                node = node.next
                if node:
                    q.put((node.val, node))
            return head.next
        
        #4th 
        # Convert merge k lists problem to merge 2 lists (\text{k-1}k-1) times.
        #Here is the merge 2 lists problem page.
        # Time complexity : O(kN) where k is the number of linked lists.
        
        
        
        #5th
        
        # This approach walks alongside the one above but is improved a lot. We don't need to traverse most nodes many times repeatedly
        # Time complexity : O(N\log k)O(Nlogk) where \text{k}k is the number of linked lists.
         '''
        Pair up \text{k}k lists and merge each pair.
        
        After the first pairing, k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.
        
        Repeat this procedure until we get the final sorted linked list.
        
        Thus, we'll traverse almost N nodes per pairing and merging, and repeat this procedure about \log_{2}{k} times.
        '''
        
        
        
        
        
        
        
        
        
        
        
        
        
        