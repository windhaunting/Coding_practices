#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:11:40 2018

@author: fubao
"""



#  114. Flatten Binary Tree to Linked List

'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        
        
        #1st use iterative dfs
        
        #  it is DFS so u need a stack. Dont forget to set the left child to null, or u’ll get TLE. (tricky!)

        # java code here
       public void flatten(TreeNode root) {
            if (root == null) return;
            Stack<TreeNode> stk = new Stack<TreeNode>();
            stk.push(root);
            while (!stk.isEmpty()){
                TreeNode curr = stk.pop();
                if (curr.right!=null)  
                     stk.push(curr.right);
                if (curr.left!=null)  
                     stk.push(curr.left);
                if (!stk.isEmpty()) 
                     curr.right = stk.peek();
                curr.left = null;  // dont forget this!! 
            }
        }
            
        
        '''
            
             *
               /
              n
           /     \\
         left   right
          \\ 
           *
            *
             \\
              p
        The idea is very simple. Suppose n is the current visiting node, and p is the previous node of preorder traversal to n.right.
        
        We just need to do the inorder replacement:
        
        n.left -> NULL
        
        n.right - > n.left
        
        p->right -> n.right
        '''
        
        
        prev = None
        def flatten(self, root):
            if not root:
                return
            self.prev = root
            self.flatten(root.left)
        
            temp = root.right
            root.right, root.left = root.left, None
            self.prev.right = temp
        
            self.flatten(temp)


        

