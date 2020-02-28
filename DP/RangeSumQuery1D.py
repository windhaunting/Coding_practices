#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:13:57 2018

@author: fubao
"""


#  303. Range Sum Query - Immutable  307. Range Sum Query - Mutable

 

'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

'''


# reference:  https://leetcode.com/problems/range-sum-query-immutable/solution/


'''
Imagine that we pre-compute the cummulative sum from index 00 to kk. Could we use this information to derive Sum(i, j)Sum(i,j)?

Let us define sum[k] as the cumulative sum for nums[0... k-1](inclusive):


Now, we can calculate sumRange as following:

sumRange(i, j) = sum[j + 1] - sum[i]

'''


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums: 
            self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int 
        :type j: int
        :rtype: int 
        """
        return self.accu[j + 1] - self.accu[i]





# 307. Range Sum Query - Mutable


'''

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

'''



# reference:

# https://leetcode.com/problems/range-sum-query-mutable/solution/



#2nd  (Sqrt decomposition) 
'''
The idea is to split the array in blocks with length of \sqrt{n}
​
​. Then we calculate the sum of each block and store it in auxiliary memory b.
 To query RSQ(i, j), we will add the sums of all the blocks lying inside and those that
 partially overlap with range [i \ldots j][i…j].

#  Time complexity : O(n)O(n) - preprocessing, O(\sqrt{n}) - range sum query, O(1)O(1) - update query


'''


# 3rd   (Segment tree) 区间树 

or binary index tree

# reference: http://www.cnblogs.com/grandyang/p/4985506.html

# other related tree:  https://stackoverflow.com/questions/17466218/what-are-the-differences-between-segment-trees-interval-trees-binary-indexed-t
#


'''
Segment tree is a very flexible data structure, because it is used to solve numerous range query problems
like finding minimum, maximum, sum, greatest common divisor, least common denominator in array in logarithmic time.

'''

The segment tree for array a[0, 1,...,n-1] is a binary tree in which 
each node contains aggregate information (min, max, sum, etc.) for a subrange[i…j] of the array, as its left and 
right child hold information for range [i... (i+j)/2]and [(i+j)/2 + 1, j]

Segment tree could be implemented using either an array or a tree. For an array implementation,
 if the element at index ii is not a leaf, its left and right child are stored at index 2i and 2i+1 respectively.:
     
1. Build segment tree

We will use a very effective bottom-up approach to build segment tree. We already know from the above that if
 some node pp holds the sum of [i \ldots j][i…j] range, its left and right children hold
 the sum for range [i... (i+j)/2]and [(i+j)/2 + 1, j] respectively.

Therefore to find the sum of node pp, we need to calculate the sum of its right and left child in advance.
We begin from the leaves, initialize them with input array elements a[0, 1, ..., n-1]. 
Then we move upward to the higher level to calculate the parents' sum till we get to the root of the segment tree.


'''
int[] tree;
int n;
public NumArray(int[] nums) {
    if (nums.length > 0) {
        n = nums.length;
        tree = new int[n * 2];
        buildTree(nums);
    }
}
private void buildTree(int[] nums) {
    for (int i = n, j = 0;  i < 2 * n; i++,  j++)
        tree[i] = nums[j];
    for (int i = n - 1; i > 0; --i)
        tree[i] = tree[i * 2] + tree[i * 2 + 1];
}

'''

2. Update segment tree

When we update the array at some index ii we need to rebuild the segment tree, because there are tree nodes which contain the sum of the modified element. Again we will use a bottom-up approach. We update the leaf node that stores a[i]a[i]. From there we will follow the path up to the root updating the value of each parent as a sum of its children values.

Java

void update(int pos, int val) {
    pos += n;
    tree[pos] = val;
    while (pos > 0) {
        int left = pos;
        int right = pos;
        if (pos % 2 == 0) {
            right = pos + 1;
        } else {
            left = pos - 1;
        }
        // parent is updated after child is updated
        tree[pos / 2] = tree[left] + tree[right];
        pos /= 2;
    }
}
        
        
3. Range Sum Query 


We can find range sum query [L, R][L,R] using segment tree in the following way:

Algorithm hold loop invariant:

l≤r and sum of [L…l] and [r…R] has been calculated, where ll and rr are the left and right boundary of calculated sum. Initially we set ll with left leaf LL and rr with right leaf RR. Range [l, r][l,r] shrinks on each iteration till range borders meets after approximately \log nlogn iterations of the algorithm

Loop till l≤r
Check if ll is right child of its parent PP
l is right child of PP. Then PP contains sum of range of l and another child which is outside the range [l,r]
 and we dont need parent PP sum. Add ll to sumsum without its parent PP and set ll to point to the right of P on the upper level.
l is not right child of PP. Then parent PP contains sum of range which lies in [l,r]. Add P to sumsum and set ll to point to the parent of PP
Check if rr is left child of its parent PP
r is left child of P. Then PP contains sum of range of  and another child which is outside the range [l, r][l,r] and 
we dont need parent P sum. Add rr to sumsum without its parent PP and set rr to point to the left of PP on the upper level.
r is not left child of PP. Then parent PP contains sum of range which lies in [l,r]. Add P to sumsum and set rr to point to the parent of PP
Java

public int sumRange(int l, int r) {
    // get leaf with value 'l'
    l += n;
    // get leaf with value 'r'
    r += n;
    int sum = 0;
    while (l <= r) {
        if ((l % 2) == 1) {
           sum += tree[l];
           l++;
        }
        if ((r % 2) == 0) {
           sum += tree[r];
           r--;
        }
        l /= 2;
        r /= 2;
    }
    return sum;
}
Complexity Analysis

Time complexity : O(\log n)O(logn)

Time complexity is O(\log n)O(logn) because on each iteration of the algorithm we move one level up, either to the parent of the current node or to the next sibling of parent to the left or right direction till the two boundaries meet. In the worst-case scenario this happens at the root after \log nlogn iterations of the algorithm.

Space complexity : O(1)O(1).


