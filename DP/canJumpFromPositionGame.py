#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:03:44 2018

@author: fubao
"""

#  55. Jump Game



'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

'''



'''
This is a dynamic programming question. Usually, solving and fully understanding a dynamic programming problem is a 4 step process:

Start with the recursive backtracking solution
Optimize by using a memoization table (top-down[3] dynamic programming)
Remove the need for recursion (bottom-up dynamic programming)
Apply final tricks to reduce the time / memory complexity

'''

# reference:  https://leetcode.com/problems/jump-game/solution/

'''
1st Time complexity : O(2^n) There are 2^n2  (upper bound) ways of jumping from the first position to the last, 
Approach #1 (Backtracking) [Stack Overflow]

This is the inefficient solution where we try every single jump pattern that takes us from the first position to the last. We start from the first position and jump to every index that is reachable. We repeat the process until last index is reached. When stuck, backtrack.


# Java Code naive 


public class Solution {
    public boolean canJumpFromPosition(int position, int[] nums) {
        if (position == nums.length - 1) {
            return true;
        }

        int furthestJump = Math.min(position + nums[position], nums.length - 1);
        for (int nextPosition = position + 1; nextPosition <= furthestJump; nextPosition++) {
            if (canJumpFromPosition(nextPosition, nums)) {
                return true;
            }
        }

        return false;
    }

    public boolean canJump(int[] nums) {
        return canJumpFromPosition(0, nums);
    }
}
    
    
    
#2nd memoizaition: Time complexity : O(n^2) too For every element in the array, say i, 
we are looking at the next nums[i] elements to its right aiming to find a GOOD index.
 nums[i] can be at most n, where n is the length of array nums.
    
for each position in the array, we remember whether the index is good or bad. 
Let's call this array memo and let its values be either one of: GOOD, BAD, UNKNOWN. 
This technique is called memoization

'''
'''
enum Index {
    GOOD, BAD, UNKNOWN
}

public class Solution {
    Index[] memo;

    public boolean canJumpFromPosition(int position, int[] nums) {
        if (memo[position] != Index.UNKNOWN) {
            return memo[position] == Index.GOOD ? true : false;
        }

        int furthestJump = Math.min(position + nums[position], nums.length - 1);
        for (int nextPosition = position + 1; nextPosition <= furthestJump; nextPosition++) {
            if (canJumpFromPosition(nextPosition, nums)) {
                memo[position] = Index.GOOD;
                return true;
            }
        }

        memo[position] = Index.BAD;
        return false;
    }

    public boolean canJump(int[] nums) {
        memo = new Index[nums.length];
        for (int i = 0; i < memo.length; i++) {
            memo[i] = Index.UNKNOWN;
        }
        memo[memo.length - 1] = Index.GOOD;
        return canJumpFromPosition(0, nums);
    }
}
        
'''

# 3rd  O(n^2)  DP top-down again without recursive
'''
that we only ever jump to the right. This means that if we start from the right of the array, 
every time we will query a position to our right, that position has already be determined as
 being GOOD or BAD. 

'''
'''
enum Index {
    GOOD, BAD, UNKNOWN
}

public class Solution {
    public boolean canJump(int[] nums) {
        Index[] memo = new Index[nums.length];
        for (int i = 0; i < memo.length; i++) {
            memo[i] = Index.UNKNOWN;
        }
        memo[memo.length - 1] = Index.GOOD;

        for (int i = nums.length - 2; i >= 0; i--) {
            int furthestJump = Math.min(i + nums[i], nums.length - 1);
            for (int j = i + 1; j <= furthestJump; j++) {
                if (memo[j] == Index.GOOD) {
                    memo[i] = Index.GOOD;
                    break;
                }
            }
        }

        return memo[0] == Index.GOOD;
    }
}

'''

# Greedy algorithm 4th O(n) 

'''
Iterating right-to-left, for each position we check if there is a potential jump that reaches
 a GOOD index (currPosition + nums[currPosition] >= leftmostGoodIndex). If we can reach a GOOD index,
 then our position is itself GOOD. Also, this new GOOD position will be the new leftmost GOOD index. 
 Iteration continues until the beginning of the array. If first position is a GOOD index then
 we can reach the last index from the first position.
'''
'''
public class Solution {
    public boolean canJump(int[] nums) {
        int lastPos = nums.length - 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (i + nums[i] >= lastPos) {
                lastPos = i;
            }
        }
        return lastPos == 0;
    }
}
'''

    
    