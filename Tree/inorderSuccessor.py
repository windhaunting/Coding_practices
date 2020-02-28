#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 22:11:34 2018

@author: fubao
"""


'''

#  Inorder Successor in BST      facebook


Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Example 1:

Input: root = [2,1,3], p = 1

  2
 / \
1   3

Output: 2
Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /   
1

Output: null

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        '''
        #1st idea use inorder traverse, when it visit p and check the next point; it generally for any tree
        # there are recursive and iterative way to do inorder. here it use iterative way first
        # seems it doesn't not utilize BST property
        
        current = root
        done = 0
        s = []     # stack
        ind = 0
        while (not done):
            if current is not None:
                s.append(current)
                current = current.left
            else:
                if len(s) > 0:
                    current = s.pop(-1)
                    if ind == 1:
                        return current
                        
                    if current == p:
                        ind = 1
                    current = current .right
                else:
                    done = 1
        return None
        '''
        # 2 use BST property, use recursive way # inorder traverse. If p's value < root.val, check left's node as new root,
        if root is None:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left is not None else root
        
        
        
        
        