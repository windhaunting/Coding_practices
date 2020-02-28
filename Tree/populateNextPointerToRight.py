#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 23:16:11 2018

@author: fubao
"""

'''
117. Populating Next Right Pointers in Each Node II              # facebook


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
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL

'''


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # Base Case
        if not root:
#            return
        d = []         #queue
        d.append(root)
        resLst = []
        while(len(d)):
            n = len(d)
            lst = []
            
            while(n > 0):
                node = d.pop(0)
                #lst.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
                
                if n == 1:
                    node.next = None
                else:
                    #print ("d: ", n, d)
                    node.next = d[0]
                n -= 1

            #resLst.append(lst)
        #print (resLst)
    #return resLst

