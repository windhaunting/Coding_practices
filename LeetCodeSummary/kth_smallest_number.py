#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:44:09 2020

@author: fubao
"""


# from educative.io

# kth smallest number:


# 
"""

Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

"""


1. 1. Brute-force #
The simplest brute-force algorithm will be to find the Kth smallest number in a step by step fashion. 

This means that, first, we will find the smallest element, then 2nd smallest, 

then 3rd smallest and so on, until we have found the Kth smallest element. Here is what the algorithm will look like:
    
    
    
import math


def find_Kth_smallest_number(nums, k):
  # to handle duplicates, we will keep track of previous smallest number and its index
  previousSmallestNum, previousSmallestIndex = -math.inf, -1
  currentSmallestNum, currentSmallestIndex = math.inf, -1
  for i in range(k):
    for j in range(len(nums)):
      if nums[j] > previousSmallestNum and nums[j] < currentSmallestNum:
        # found the next smallest number
        currentSmallestNum = nums[j]
        currentSmallestIndex = j
      elif nums[j] == previousSmallestNum and j > previousSmallestIndex:
        # found a number which is equal to the previous smallest number; since numbers can repeat,
        # we will consider 'nums[j]' only if it has a different index than previous smallest
        currentSmallestNum = nums[j]
        currentSmallestIndex = j
        break  # break here as we have found our definitive next smallest number

    # current smallest number becomes previous smallest number for the next iteration
    previousSmallestNum = currentSmallestNum
    previousSmallestIndex = currentSmallestIndex
    currentSmallestNum = math.inf

  return previousSmallestNum


The time complexity of the above algorithm will be O(N*K). The algorithm runs in constant space O(1)O(1).




2. Brute-force using Sorting #
We can use an in-place sort like a HeapSort to sort the input array to get the Kth smallest number. Following is the code for this solution:
    
    
def find_Kth_smallest_number(nums, k):
  return sorted(nums)[k-1]

Sorting will take O(NlogN) and if we are not using an in-place sorting algorithm, we will need O(N) space.




3. Using Max-Heap #
As discussed in Kth Smallest Number, we can iterate the array and use a Max Heap to keep track of ‘K’ smallest number. In the end, the root of the heap will have the Kth smallest number.


from heapq import *
def find_Kth_smallest_number(nums, k):
  maxHeap = []
  # put first k numbers in the max heap
  for i in range(k):
    heappush(maxHeap, -nums[i])

  # go through the remaining numbers of the array, if the number from the array is smaller than the
  # top(biggest) number of the heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if -nums[i] > maxHeap[0]:
      heappop(maxHeap)
      heappush(maxHeap, -nums[i])

  # the root of the heap has the Kth smallest number
  return -maxHeap[0]


Time & Space Complexity #
The time complexity of the above algorithm is O(K*logK + (N-K)*logK) which is asymptotically equal to O(N*logK). The space complexity will be O(K) because we need to store ‘K’ smallest numbers in the heap.

4. Using Min-Heap #
Also discussed in Kth Smallest Number, we can use a Min Heap to find the Kth smallest number. We can insert all the numbers in the min-heap and then extract the top ‘K’ numbers from the heap to find the Kth smallest number.

Time & Space Complexity #
Inserting all numbers in the heap will take O(N*logN) and extracting ‘K’ numbers will take O(K*logN). Overall, the time complexity of this algorithm will be O(N*logN+K*logN) and the space complexity will be O(N).




5. Using Partition Scheme of Quicksort #
Quicksort picks a number called pivot and partition the input array around it. After partitioning, all numbers smaller than the pivot are to the left of the pivot, and all numbers greater than or equal to the pivot are to the right of the pivot. This ensures that the pivot has reached its correct sorted position.

We can use this partitioning scheme to find the Kth smallest number. We will recursively partition the input array and if, after partitioning, our pivot is at the K-1 index we have found our required number; if not, we will choose one the following option:

If pivot’s position is larger than K-1, we will recursively partition the array on numbers lower than the pivot.
If pivot’s position is smaller than K-1, we will recursively partition the array on numbers greater than the pivot.


def find_Kth_smallest_number_rec(nums, k, start, end):
  p = partition(nums, start, end)

  if p == k - 1:
    return nums[p]

  if p > k - 1:  # search lower part
    return find_Kth_smallest_number_rec(nums, k, start, p - 1)

  # search higher part
  return find_Kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, low, high):
  if low == high:
    return low

  pivot = nums[high]
  for i in range(low, high):
    # all elements less than 'pivot' will be before the index 'low'
    if nums[i] < pivot:
      nums[low], nums[i] = nums[i], nums[low]
      low += 1

  # put the pivot in its correct place
  nums[low], nums[high] = nums[high], nums[low]
  return low


The above algorithm is known as QuickSelect and has a Worst case time complexity of O(N^2). 
The best and average case is O(N) , which is better than the best and average case of QuickSort.
 Overall, QuickSelect uses the same approach as QuickSort i.e., partitioning the data into two parts based on a pivot. 
 However, contrary to QuickSort, instead of recursing into both sides QuickSelect only recurses into one side – the side with the element it is searching for. 
 This reduces the average and best case time complexity from O(N*logN) to O(N).
 The worst-case occurs when, at every step, the partition procedure splits the N-length array into arrays of size ‘11’ and ‘N−1’. 
 This can only happen when the input array is sorted or if all of its elements are the same. This “unlucky” selection of pivot elements requires O(N) recursive calls, leading to an O(N^2) worst-case.

Worst-case space complexity will be O(N) used for the recursion stack. 



6. Using Randomized Partitioning Scheme of Quicksort #

 As mentioned above, the worst case for Quicksort occurs when the partition procedure splits the N-length array into arrays of size ‘11’ and ‘N−1’. 
 To mitigate this, instead of always picking a fixed index for pivot 
 (e.g., in the above algorithm we always pick nums[high] as the pivot),
 we can randomly select an element as pivot. After randomly choosing the pivot element, 
 we expect the split of the input array to be reasonably well balanced on average.


import random


def find_Kth_smallest_number(nums, k):
  return find_Kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


def find_Kth_smallest_number_rec(nums, k, start, end):
  p = partition(nums, start, end)

  if p == k - 1:
    return nums[p]

  if p > k - 1:  # search lower part
    return find_Kth_smallest_number_rec(nums, k, start, p - 1)

  # search higher part
  return find_Kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, low, high):
  if low == high:
    return low

  pivotIndex = random.randint(low, high)
  nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]

  pivot = nums[high]
  for i in range(low, high):
    # all elements less than 'pivot' will be before the index 'low'
    if nums[i] < pivot:
      nums[low], nums[i] = nums[i], nums[low]
      low += 1

  # put the pivot in its correct place
  nums[low], nums[high] = nums[high], nums[low]
  return low
