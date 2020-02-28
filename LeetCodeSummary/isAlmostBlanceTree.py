#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:51:13 2018

@author: fubao
"""


# 110. Balanced Binary Tree
'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''

# check almost balanced tree

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
        
        #1st DFS ; but lots of repetition of recursive with recursive in calling maxDepth for each node
        # while traversing, judge every leaf node's depth and record the maximum and minimum depth, if maximum depth is 2 more than minimum depth, that is an unbalanced tree
        if not root:
            return True
        st = []
        st.append(root)
        while(len(st)):
            node = st.pop()
            
            if math.fabs(maxDepth(node.left) - maxDepth(node.right)) > 1:
                return False
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return True
         
        def maxDepth(node):        #complexity o(n)
            if not node:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))
        
        
        #2nd       complexity is very high; ?   worst case O(n) + 2*o(n/2) + 4*o(n/4)   => O(nlogn) 
        if not root:
            return True
        if math.fabs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        '''
        
        
        #3rd best recursive so far?
        if not root:
            return True
        ret = self.balanceHelper(root)
        if (ret == -1):
            return False
        return True
        
    def balanceHelper(self, node):
        if not node:
            return 0
        left = self.balanceHelper(node.left)
        if (left == -1):                 #why?  check left or right already skewed more than by 1 in subtree
            return -1
        right = self.balanceHelper(node.right)
        if right == -1:
            return -1
        if (left-right) > 1 or (right-left) > 1:
            return -1
            
        return 1 + max(left, right)

    

    #4th  use iterative way ;  based on postorder traversal idea
    
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
        
        
        
   # 5th or use bfs traversing
    从上往下扫，记录level，第一次扫描到叶子结点，记录当前深度，继续向下扫，以后每次遇到叶子结点都拿level和记录的一个深度比较，
    如果大于1就返回false，直到扫完所有结点 o(n)复杂度。