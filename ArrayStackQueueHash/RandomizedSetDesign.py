#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:56:09 2018

@author: fubao
"""

# 380. Insert Delete GetRandom O(1)

'''
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

'''


# import random
class RandomizedSet(object):

    
    # use array for get random linearly, array store the values; 
    #hashmap to store the value and the index in the array;
    # for removing a value, swap the value with the last element in the array; 
    #From Python docs (https://wiki.python.org/moin/TimeComplexity) we know that list.append() takes O(1), both average and amortized. Dictionary get and set functions take O(1) average, so we are OK.
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.posDic = [], {}

        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.posDic:
            self.nums.append(val)
            self.posDic[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.posDic:
            idx, last = self.posDic[val], self.nums[-1]
            self.nums[idx], self.posDic[last] = last, idx
            self.nums.pop(); 
            self.posDic.pop(val, 0)
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        #return random.choice(list(self.dic.keys()))           #is it average o(1) time no; list() o(n)time;   or use randint from array; o(1)  or use reservoir sampling (but o(n)) too?
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()