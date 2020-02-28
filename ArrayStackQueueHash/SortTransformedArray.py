#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 00:16:36 2018

@author: fubao
"""




# 360. Sort Transformed Array  square sorted array


'''
Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)


Example:

nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]


'''



'''
思路: 当a>0时,抛物线开口向上,这样给定的数组最大值肯定是在两端, 也就是要么在数组开始,要么在数组的最后, 这样我们可以依次取得最大值.最后的时候翻转一下数组即可.
当a<0时, 抛物线开口向下,这样最小值肯定也是在两端, 我们可以依次在两端取最小值.
'''

    

#  c++ code    
    
class Solution {  
public:  
    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {  
        if(nums.size() ==0) return {};  
        vector<int> result;  
        int left = 0, right = nums.size()-1;  
        auto func = [=](int x) { return a*x*x + b*x + c; };  
        while(left <= right)  
        {  
            int val1 = func(nums[left]), val2 = func(nums[right]);  
            if(a > 0) result.push_back(val1>=val2?val1:val2);  
            if(a > 0) val1>val2?left++:right--;  
            if(a <= 0) result.push_back(val1>=val2?val2:val1);  
            if(a <= 0) val1>val2?right--:left++;  
        }  
        if(a > 0) reverse(result.begin(), result.end());  
        return result;  
    }  
};  
