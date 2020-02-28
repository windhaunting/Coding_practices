#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:32:16 2018

@author: fubao
"""


# 116. Populating Next Right Pointers in Each Node


'''
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL

'''


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        '''
        #1st  level order traversal idea to use stack, but not constance space?
        '''
        #        1
        #     2       3
        #  4    5   6   7
        #8  9 10 11
        '''
        if root is None:
            return None
        p = root
        que = [root]      # as queue
        while(len(que)):
            #pop
            n = len(que)
            while(n > 0):
                nd = que.pop(0)
                if n== 1:
                    nd.next = None
                else:
                    nd.next = que[0]
                if nd.left is not None:
                    que.append(nd.left)
                if nd.right is not None:
                    que.append(nd.right)
                n -= 1
        '''               
        #2nd use recursive
        if not root or not root.left:
            return 
        self.connect(root.left)
        self.connect(root.right)
        left  = root.left 
        right = root.right 
        while left:
            left.next = right 
            left  = left.right 
            right = right.left 
            
        
        