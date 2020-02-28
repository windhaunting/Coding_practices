#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:03:20 2018

@author: fubao
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




#173. Binary Search Tree Iterator

#https://leetcode.com/problems/binary-search-tree-iterator/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = []
        self.getAllLeftNode(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        
        return (len(self.stk) != 0)

    def next(self):
        """
        :rtype: int
        """
        #pop from stack
        node = self.stk.pop()
        self.getAllLeftNode(node.right)
        return node.val
    
    def getAllLeftNode(self, node):
        '''
        get the most left nodes and put in the stack
        '''
        while (node is not None):
            self.stk.append(node)
            node = node.left
            
        
        
        
