#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:44:22 2018

@author: fubao
"""



#  Given preorder and inorder traversal of a tree, construct the binary tree.

'''
Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        inordInd = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:inordInd+1], inorder[0:inordInd])
        root.right = self.buildTree(preorder[inordInd+1:], inorder[inordInd+1:])
        return root