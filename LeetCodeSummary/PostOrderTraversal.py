#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 09:46:03 2018

@author: fubao
"""


#  145. Binary Tree Postorder Traversal




# reference:  https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/


'''

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

'''



#use one stack to simulate  reverse postorder


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        

#  postorder traversal

'''
    1
  2   3
4

4 2 3 1
'''


    
#1st recursive way  postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.val),
 
    

#iterative way The first is by postorder using a flag to indicate whether the node has been visited or not.

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return traversal
    

#The 2nd uses modified preorder (right subtree first). Then reverse the result.

    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversalSecondSolution(self, root):
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)       #pop first

        # reverse result
        return traversal[::-1]
    

# 2nd iterative way;        use 2 stacks
'''
1. Push root to first stack.
2. Loop while first stack is not empty
   2.1 Pop a node from first stack and push it to second stack
   2.2 Push left and right children of the popped node to first stack
3. Print contents of second stack

'''

# Python porgram for iterative postorder traversal using
# two stacks
 
# A binary tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# An iterative function to do postorder traversal of a
# given binary tree use two stacks
def postOrderIterative(root): 
 
    if root is None:
        return         
     
    # Create two stacks 
    s1 = []
    s2 = []
     
    # Push root to first stack
    s1.append(root)
     
    # Run while first stack is not empty
    while (len(s1) >0):
         
        # Pop an item from s1 and append it to s2
        node = s1.pop()
        s2.append(node)
     
        # Push left and right children of removed item to s1
        if node.left is not None:
            s1.append(node.left)
        if node.right is not None :
            s1.append(node.right)
 
        # Print all eleements of second stack
    while(len(s2) > 0):
        node = s2.pop()
        print (node.data)
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
postOrderIterative(root)


#3rd still iterative way using one stack

'''
1.1 Create an empty stack
2.1 Do following while root is not NULL
    a) Push root's right child and then root to stack.
    b) Set root as root's left child.
2.2 Pop an item from stack and set it as root.
    a) If the popped item has a right child and the right child 
       is at top of stack, then remove the right child from stack,
       push the root back and set root as root's right child.
    b) Else print root's data and set root as NULL.
2.3 Repeat steps 2.1 and 2.2 while stack is not empty.

'''

# Python program for iterative postorder traversal
# using one stack
 
# Stores the answer
ans = []
 
# A Binary tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None
# A iterative function to do postorder traversal of 
# a given binary tree
def postOrderIterative(root):
         
    # Check for empty tree
    if root is None:
        return
 
    stack = []
     
    while(True):
         
        while (root):
             # Push root's right child and then root to stack
             if root.right is not None:
                stack.append(root.right)
             stack.append(root)
 
             # Set root as root's left child
             root = root.left
         
        # Pop an item from stack and set it as root
        root = stack.pop()
 
        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before root
        if (root.right is not None and
            peek(stack) == root.right):
            stack.pop() # Remove right child from stack 
            stack.append(root) # Push root back to stack
            root = root.right # change root so that the 
                             # righ childis processed next
 
        # Else print root's data and set root as None
        else:
            ans.append(root.data) 
            root = None
 
        if (len(stack) <= 0):
                break
 
# Driver pogram to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
print ("Post Order traversal of binary tree is")
postOrderIterative(root)
print (ans)
