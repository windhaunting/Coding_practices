#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 20:01:29 2018

@author: fubao
"""
 
# 98. Validate Binary Search Tree



'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.


'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        ###1st itereatie way 1st idea is to inorder traverse and check the ordering is correct oder when traverse
        stk = []            #stack 
        preVal = -1*(2**32)           # TreeNode
        while (root or len(stk)):
            while (root is not None):
                stk.append(root)
                root = root.left
            root = stk.pop(-1)

            if root.val <= preVal:
                return False
            preVal = root.val
            root = root.right
        return True
    
        '''
        #2nd Use recursion. Pass down two parameters: floor (which means that all nodes in the the current subtree must be smaller than this value) and            ceiling (all must be larger than it). Compare root of the current subtree with these two values. Then, recursively check the left and right           subtree of  the current one. Take care of the values passed down.
        
        def isValidBSThelper(root, floor=float('-inf'), ceiling=float('inf')):
            if not root: 
                return True
            if root.val <= floor or root.val >= ceiling:           #satisfying case
                return False
            # in the left branch, root is the new ceiling; and root is the new floor in right branch
            return isValidBSThelper(root.left, floor, root.val) and isValidBSThelper(root.right, root.val, ceiling)
        return isValidBSThelper(root, float('-inf'), float('inf'))
    

# another writing method with recursive  Java code
'''
public class Solution {
    TreeNode lastNode; 
    public boolean isValidBST(TreeNode root) {
        if(root == null)
            return true;
        if(!isValidBST(root.left))
            return false;
        if(lastNode != null && lastNode.val >= root.val)
            return false;
        lastNode = root;
        if(!isValidBST(root.right))
            return false;
        return true;
    }
}
    
'''