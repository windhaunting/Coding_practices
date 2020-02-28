#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:40:45 2018

@author: fubao
"""



# 230. Kth Smallest Element in a BST



'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and 
you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #1st naive idea is to use inorder traversal, because of the characteristics of binary search tree, when the kth number is visited,
        #it is the kth smallest value     time complexity o(k),   worst time complexity o(n)
               
        # use recursive way
        self.res = None
        self.k = k

        self.bfsInorderRecursive(root)
        return self.res
        
    def bfsInorderRecursive(self, node):
        if node:
            self.bfsInorderRecursive(node.left)
            #print ("d: ", k, node.val)

            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return 
            self.bfsInorderRecursive(node.right)
     
        
        '''
        #2.or we can use iterative way, use stack to do inorder traverse when there is kth element, stop
        #maintain a list  
        current = root
        stk = []            #stack
        cnt = 1
        while (current or len(stk)):
            while current is not None:       #Reach the left most Node of the current Node
                stk.append(current)
                current = current.left
            if (len(stk) > 0):
                current = stk.pop(-1)
                if cnt == k:
                   return current.val
                cnt += 1
                current = current.right
        return -2**32
        '''
        
        
        # follow up : #storing all nodes value is also helpful if we need to find kth element frequently and BST itself could be                                                         #  altered (inserted/deleted) by multiple times, so that’s the main reason that I stored them in an array.?
        
        '''
        def bfsInorderRecursive(node, ansLst):
            if node:
                bfsInorderRecursive(node.left, ansLst)
                #print ("d: ", k, node.val)
                
                ansLst.append(node.val)               
                
                bfsInorderRecursive(node.right, ansLst)
        
        ansLst = []
        
        bfsInorderRecursive(root, ansLst)
        return ansLst[k-1]
        '''
            

