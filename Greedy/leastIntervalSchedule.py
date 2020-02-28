#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:59:07 2018

@author: fubao
"""




# Java code

# 621. Task Scheduler cool down        facebook
#
'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''
#


#  reference:  https://leetcode.com/problems/task-scheduler/solution/
'''
 Consider the case, where say the number of instances of tasks A, B, C, D, E are 6, 1, 1, 1, 1 respectively with n=2(cooling time). 
 If we go by the above method, firstly we give 1 round to each A, B, C, D and E. 
 Now, only 5 instances of A are pending, but each instance will take 3 time units to complete because of cooling time. 
 But a better way to schedule the tasks will be this: A, B, C, A, D, E, ... . 
 In this way, by giving turn to the task A as soon as its cooling time is over, 
 we can save a good number of clock cycles.

From the above example, we are clear with one idea. It is that, the tasks with the currently maximum number of outstanding (pending)instances 
will contribute to a large number of idle cycles in the future,
 if not executed with appropriate interleavings with the other tasks. Thus, we need to re-execute such a task 
 as soon as its cooling time is finished.

Thus, based on the above ideas, firstly, we obtain a count of the number of instances of each task in mapmap array. 
Then, we start executing the tasks in the order of descending number of their initial instances. 
As soon as we execute the first task, we start its cooling timer as well
(ii). For every task executed, we update the pending number of instances of the current task. 
We update the current time, timetime, at every instant as well. 
Now, as soon as the timer, ii's value exceeds the cooling time, as discussed above, 
we again need to consider the task with the largest number of pending instances. 
Thus, we again sort the taskstasks array with updated counts of instances and
 again pick up the tasks in the descending order of their number of instances.

'''
 
'''
从举例子中我们可以得出任务调度的规律。
如给定：AAABBCD，n=2。那么我们满足个数最多的任务所需的数量，即可以满足任务间隔要求，即：AXXAXXA；（其中，X表示需要填充任务或者idle的间隔）
如果有两种或两种以上的任务具有相同的最多的任务数，如：AAAABBBBCCDE，n=3。那么我们将具有相同个数的任务A和B视为一个任务对，最终满足要求的分配为：ABXXABXXABXXAB，剩余的任务在不违背要求间隔的情况下穿插进间隔位置即可，空缺位置补idle。
由上面的分析我们可以得到最终需要最少的任务时间：（最多任务数-1）*（n + 1） + （相同最多任务的任务个数）。
有上面的例子来说就是：(num(A)-1) * (3+1) + (2)。
'''



# https://blog.csdn.net/koala_tree/article/details/78498586

# also reference: https://github.com/tongzhang1994/Facebook-Interview-Coding/blob/master/Task%20schedule%20with%20cool%20down%20time.java


# http://zxi.mytechroad.com/blog/greedy/leetcode-621-task-scheduler/


from collections import defaultdict
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 1st find the principle
        
        '''
        从举例子中我们可以得出任务调度的规律。
        如给定：AAABBCD，n=2。那么我们满足个数最多的任务所需的数量，即可以满足任务间隔要求，即：AXXAXXA；（其中，X表示需要填充任务或者idle的间隔）
        如果有两种或两种以上的任务具有相同的最多的任务数，如：AAAABBBBCCDE，n=3。那么我们将具有相同个数的任务A和B视为一个任务对，最终满足要求的分配为：ABXXABXXABXXAB，剩余的任务在不违背要求间隔的情况下穿插进间隔位置即可，空缺位置补idle。
        由上面的分析我们可以得到最终需要最少的任务时间：（最多任务数-1）*（n + 1） + （相同最多任务的任务个数）。
        有上面的例子来说就是：(num(A)-1) * (3+1) + (2)。

        also, there is one special cases:
         # special case: ["A","A","A","B","B","B"] ; if ans = tasklength
        
        '''
        dictCnt = [0]*26
        maxCnt = 0
        ans = 0
        for i in tasks:
            #print ('ord[i]', ord(i))
            dictCnt[ord(i) - 65] += 1
        
            maxCnt = max(dictCnt[ord(i) - 65], maxCnt)
        dictCnt = sorted(dictCnt, reverse=True)

        j = 1
        p = 1
        while(j < len(dictCnt) ):
            if (dictCnt[0] == dictCnt[j]):
                p += 1
            else:
                break
            j += 1
        print ("dictCnt: ", dictCnt)
        ans = (maxCnt-1) *(n+1) + p
        return max(ans, len(tasks))           # special case: ["A","A","A","B","B","B"] ; if ans = tasklength
        


public class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] map = new int[26];
        for (char c: tasks)
            map[c - 'A']++;
        PriorityQueue < Integer > queue = new PriorityQueue < > (26, Collections.reverseOrder());
        for (int f: map) {
            if (f > 0)
                queue.add(f);
        }
        int time = 0;
        while (!queue.isEmpty()) {
            int i = 0;
            List < Integer > temp = new ArrayList < > ();
            while (i <= n) {
                if (!queue.isEmpty()) {
                    if (queue.peek() > 1)
                        temp.add(queue.poll() - 1);
                    else
                        queue.poll();
                }
                time++;
                if (queue.isEmpty() && temp.size() == 0)
                    break;
                i++;
            }
            for (int l: temp)
                queue.add(l);
        }
        return time;
    }
}

