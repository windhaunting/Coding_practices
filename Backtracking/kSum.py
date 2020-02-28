#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:27:25 2018

@author: fubao
"""



# K sum

'''
Given n distinct positive integers, integer k (k <= n) and a number target.

Find k numbers where sum is target. Calculate how many solutions there are?

Example

Given [1,2,3,4], k = 2, target = 5.

There are 2 solutions: [1,4] and [2,3].

Return 2.



'''

#[1,2,3,4] , k = 2, target = 5;   1 (5-1)-> 2 (5-1-2) =>  or 3 (5-1-3) => or (5-1-4) get answer
# Java code reference

public class Solution {
    /**
     * @param A: an integer array.
     * @param k: a positive integer (k <= length(A))
     * @param target: a integer
     * @return a list of lists of integer
     */
    public ArrayList<ArrayList<Integer>> kSumII(int A[], int k, int target) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> path = new ArrayList<Integer>();
        helper(res, path, A, k, target, 0);
        return res;
    }

    public void helper(ArrayList<ArrayList<Integer>> res, ArrayList<Integer> path, int[] A, int k, int remain, int index) {
        if (path.size() == k) {
            if (remain == 0) {
                res.add(new ArrayList<Integer>(path));
            }
            return;
        }
        for (int i=index; i<A.length; i++) {
            path.add(A[i]);
            helper(res, path, A, k, remain-A[i], i+1);
            path.remove(path.size()-1);
        }
    }
}