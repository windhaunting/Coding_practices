#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:37:16 2018

@author: fubao
"""

'''
冒泡排序（bubble sort）— O(n2)
鸡尾酒排序（cocktail sort）—O(n2)
插入排序（insertion sort）—O(n2)
桶排序（bucket sort）—O(n);需要O(k)额外空间
计数排序（counting sort）—O(n+k);需要O(n+k)额外空间
归并排序（merge sort）—O(n log n);需要O(n)额外空间
原地归并排序— O(n2)
二叉排序树排序（binary tree sort）— O(n log n)期望时间; O(n2)最坏时间;需要O(n)额外空间
鸽巢排序（pigeonhole sort）—O(n+k);需要O(k)额外空间
基数排序（radix sort）—O(n·k);需要O(n)额外空间

不稳定的排序[编辑]
选择排序（selection sort）—O(n2)
希尔排序（shell sort）—O(n log2 n)如果使用最佳的现在版本
Clover排序算法（Clover sort）—O(n)期望时间，O（n^2/2）最坏情况
梳排序— O(n log n)
堆排序（heap sort）—O(n log n)
平滑排序（smooth sort）— O(n log n)
    
    
    
快速排序（quick sort）—O(n log n)期望时间, O(n2)最坏情况;对于大的、乱数列表一般相信是最快的已知排序
有人点踩可能是以为是“当数组已经有序的情况下，复杂度就是o(N^2)”实际上这是有前提的，就是枢纽元pivot的选取，是直接选a[0]或则a[n-1]。这种情况下o(N^2)正是因为每次都选到了最大或者最小的元素为枢纽元！
    最坏情况是枢纽元为最大或者最小数字，那么所有数都划分到一个序列去了 时间复杂度为O(n^2)
    
    
    
平均时间复杂度由高到低为：

冒泡排序O(n2)
选择排序O(n2)
插入排序O(n2)
希尔排序O(n1.25)
堆排序O(n log n)
归并排序O(n log n)
快速排序O(n log n)
基数排序O(n)
说明：虽然完全逆序的情况下，快速排序会降到选择排序的速度，不过从概率角度来说（参考信息学理论，和概率学），不对算法做编程上优化时，快速排序的平均速度比堆排序要快一些。

'''

# the content above from other's,  not double-checked correctly or not
# there is cycle sort too


wiggle sort 
324. Wiggle Sort II

