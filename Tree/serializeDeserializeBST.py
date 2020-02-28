#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:01:26 2019

@author: fubao
"""


# facebook 
'''
449. Serialize and Deserialize BST
Medium

822

55

Favorite

Share
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

'''
 
#SUCCESS idea 1: utilizing the BST tree characteristics, the left node value is always to be lower than the root,  the right node value is always to be higher than the root.
# serialize as preorder. e.g. 10 7 4 8 12 13 nodes smaller than 10 falls in the left part, nodes bigger than 10 falls the right part, and in the left part, 7 is the new root, nodes smaller than 7 falls left part, nodes bigger than 7 is the right children nodes
# then deserialize according to the property recursively
# hence, preorder the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # serialize
        res = []
        self.serializeHelper(root, res)
       
        #print ("res:" , " ". join(str(r) for r in res))
        
        return ",". join(str(r) for r in res)
    
    def serializeHelper(self, node, res):
        if node is not None:
            res.append(node.val)
            self.serializeHelper(node.left, res)
            self.serializeHelper(node.right,res)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        # 
        :type data: str
        :rtype: TreeNode
        """
        if data is " " or len(data) == 0:
            return None
        
        # 10 7 4 8 12 13
        data = [int(e) for e in data.split(",")]
        
        low = 0
        high = len(data)-1
        
        return self.deserializeHelper(data, low, high)
        
    def deserializeHelper(self, data, low, high):
        
        
        if low > high:
            return None
        #print(", ", low, high)
        nd = TreeNode(data[low])
        # find subdivision
        rootVal = nd.val
        middle= self.findDivision(data, rootVal, low+1, high)
        #print ("middle: ", middle)
        nd.left = self.deserializeHelper(data, low+1, middle-1)
        nd.right = self.deserializeHelper(data, middle, high)
        
        return nd
    
    def findDivision(self, data, rootVal, low, high):
        
        for i in range(low, high+1):
            if data[i] > rootVal:
                return i

        return high+1         
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))