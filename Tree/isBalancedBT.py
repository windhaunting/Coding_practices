#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:08:18 2018

@author: fubao
"""



#  110. Balanced Binary Tree

'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        #1st DFS  worst case O(NLOGN) while traversing, judge every leaf node's depth and record the maximum and minimum depth, if maximum depth is 2 more than minimum depth, that is an unbalanced tree
        if not root:
            return True
        st = []
        st.append(root)
        while(len(st)):
            node = st.pop()
            
            if math.fabs(self.maxDepth(node.left) - self.maxDepth(node.right)) > 1:
                return False
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return True
                
        
        '''
        #2nd       complexity is very high; ?   worst case O(n) + 2*o(n/2) + 4*o(n/4)   => O(nlogn) 
        if not root:
            return True
        if math.fabs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        '''
        
    def maxDepth(self, node):        #complexity o(n)
        if not node:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
        
        
        
        '''
        #3rd recursive    #judge left and right height,  termination in the process   O(n)
        if not root:
            return True
        ret = self.balanceHelper(root)
        if (ret == -1):
            return False
        return True
        '''
        
    def balanceHelper(self, node):
        if not node:
            return 0
        left = self.balanceHelper(node.left)
        if (left == -1):
            return -1
        right = self.balanceHelper(node.right)
        if right == -1:
            return -1
        if (left-right) > 1 or (right-left) > 1:
            return -1
        if left > right:
            return left + 1
        else:
            return right + 1
        
        
        