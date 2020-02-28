#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 23:19:59 2018

@author: fubao
"""

# level traversal  recursive and iterative


'''
#1st Recursive Python program for -
 traversal of Binary Tree
 
# A node structure
class Node:
 
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None
        

# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)

def printGivenLevel(root , level):
    if root is None:
        return
    if level == 1:
        print ("%d" , (root.data))
    elif level > 1 :
        printGivenLevel(root.left , level-1)
        printGivenLevel(root.right , level-1)
    
    
def height(node):
    if node is None:
        return 0
    else :
        # Compute the height of each subtree 
        lheight = height(node.left)
        rheight = height(node.right)
 
        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1
        
     # return 1 + max(height(node.left), height(node.right))       # or use this line
     
     
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level order traversal of binary tree is -")
printLevelOrder(root)

printGivenLevel(root, 3)

'''

# 2nd iterative way
# or we can use BFS store the node and the level  queue.append((node, level)) to acchieve this purpose?

# A node structure
from collections import deque

class Node:
    # A utility function to create a new node
    def __init__(self ,key):
        self.val = key
        self.left = None
        self.right = None
 
# Iterative Method to print the height of binary tree
def printLevelOrder(root):
   # Base Case
    if not root:
        return []
    d = deque()
    d.append(root)
    resLst = []
    while(len(d)):
        n = len(d)
        lst = []
        while(n > 0):
            node = d.popleft()
            lst.append(node.val)
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)
            n -= 1
        resLst.append(lst)
    print (resLst)
    return resLst
 
#Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level Order Traversal of binary tree is -")
printLevelOrder(root)


# reverse level order traversal

# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Function to print reverse level order traversal
def reverseLevelOrder(root):
    h = height(root)
    for i in reversed(range(1, h+1)):
        printGivenLevel(root,i)

# Print nodes at a given level
def printGivenLevel(root, level):
 
    if root is None:
        return
    if level == 1 :
        print (root.data)
    elif level>1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)
 
# Compute the height of a tree-- the number of 
# nodes along the longest path from the root node
# down to the farthest leaf node
def height(node):
    if node is None:
        return 0
    else:
 
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight :
            return lheight + 1
        else:
            return rheight + 1
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Level Order traversal of binary tree is")
reverseLevelOrder(root)
