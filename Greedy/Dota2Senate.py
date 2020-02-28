#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:07:08 2019

@author: fubao
"""

# 649. Dota2 Senate

'''
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right:
A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory:
If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and make the decision about the change in the game.
 

Given a string representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party respectively. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be Radiant or Dire.

Example 1:

Input: "RD"
Output: "Radiant"
Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights any more since his right has been banned. 
And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
 

Example 2:

Input: "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in the round 1. 
And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
'''



class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        
        # 1st error: misunderstanding;  does it only ban the adjcent's opposing team's voter? or the rest of senators.
        #Is this the rule we found?
        # count how many R and D
        # if they are equal, which has the first letter wins
        # if not, which has the most members wins?
        '''
        if senate == None or len(senate) == 0:
            return None
        num_r = 0
        num_d = 0
        for i in range(0, len(senate)):
            if senate[i] == 'R':
                num_r += 1
            elif senate[i] == 'D':
                num_d += 1
        
        if num_r == num_d:
            if senate[0] == "R":
                return "Radiant"
            else:
                return "Dire"
        elif num_r > num_d:
            return "Radiant"
        else:
            return "Dire"
        '''
        '''
        #2nd brute force TLE 单暴力的方法就是先统计所有R和D的个数，然后从头开始遍历，如果遇到了R，就扫描之后所有的位置，然后还要扫描R前面的位置，这就要用到数组的环形遍历的知识了，其实就是坐标对总长度取余，使其不会越界，如果我们找到了下一个D，就将其标记为B，然后对应的计数器cntR自减1。对于D也是同样处理，我们的while循环的条件是cntR和cntD都要大于0，当有一个等于0了的话，那么推出循环，返回那个不为0的阵营即可
        #because it call bans one senator's right which do not to be adjacent to him
        # use brute force method, find all the other opposing team's senator in a circular way
        
        num_r = 0
        num_d = 0
        
        for i in range(0, len(senate)):
            if senate[i] == 'R':
                num_r += 1
            elif senate[i] == 'D':
                num_d += 1
                
        while (num_r > 0 and num_d > 0):
            for i in range(0, len(senate)):
                if senate[i] == 'R':
                    for j in range(i+1, i+len(senate)):
                        if senate[j%len(senate)] == 'D':
                            senate = senate[:j%len(senate)] + 'B' + senate[j%len(senate)+1:]
                            num_d -= 1
                            break
                elif senate[i] == 'D':
                    for j in range(i+1, i+len(senate)):
                        if senate[j%len(senate)] == 'R':
                            senate = senate[:j%len(senate)] + 'B' + senate[j%len(senate)+1:]
                            num_r -= 1
                            break
        if num_r != 0:
            return "Radiant"
        else:
            return "Dire"
            
        '''   
            
        
        # 3rd optimize, it takes O(N^2)-O(N^3) time to finish with brute force algorithm
        # how to optimize   ref: https://www.cnblogs.com/grandyang/p/7439222.html
        # 把各自阵营的位置存入不同的队列里面，然后进行循环，每次从两个队列各取一个位置出来，看其大小关系，小的那个说明在前面，就可以把后面的那个Ban掉，所以我们要把小的那个位置要加回队列里面，但是不能直接加原位置，因为下一轮才能再轮到他来Ban，所以我们要加上一个n，再排入队列。这样当某个队列为空时，退出循环，我们返回不为空的那个阵营.
        from collections import deque
        q_r = deque()
        q_n = deque()
        for i in range(0, len(senate)):
            if senate[i] == 'R':
                q_r.append(i)
            else:
                q_n.append(i)
        
        while (len(q_r) and len(q_n)):
            e_r = q_r.popleft()
            e_n = q_n.popleft()
            if e_r < e_n:  # put the index back into the list
                q_r.append(e_r+len(senate))
            else:
                q_n.append(e_n+len(senate))
        
        if len(q_r):
            return "Radiant"
        else:
            return "Dire"
        
        
        