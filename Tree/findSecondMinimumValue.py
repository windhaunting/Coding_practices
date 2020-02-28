#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 09:57:40 2018

@author: fubao
"""




'''

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.


'''


'''
case

         2
      2     5
   4     3
  
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


  
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        #1st brute force   
        # Traverse the tree with a depth-first search, and record every unique value in the tree using a Set structure uniques.
        #Then, we'll look through the recorded values for the second minimum. The first minimum must be \text{root.val}root.val.

        def dfs(node):
            if node:
                uniques.add(node.val)
                dfs(node.left)
                dfs(node.right)

        uniques = set()
        dfs(root)

        min1, ans = root.val, float('inf')
        for v in uniques:
            if min1 < v < ans:
                ans = v

        return ans if ans < float('inf') else -1
    
    
    
    # 2nd 
    #Let min1 = root.val When traversing the tree at some node, node, if node.val > min1, we know all values in the subtree at node are at least node.val,
    #so there cannot be a better candidate for the second minimum in this subtree. Thus, we do not need to search this subtree.

    #Also, as we only care about the second minimum ans, we do not need to record any values that are larger than our current candidate for the second minimum,
    #so unlike Approach #1 we can skip maintaining a Set of values(uniques) entirely.


        self.ans = float('inf')
        min1 = root.val
    
        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)
    
        dfs(root)
        return self.ans if self.ans < float('inf') else -1



