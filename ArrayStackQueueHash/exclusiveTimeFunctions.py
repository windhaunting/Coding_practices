#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 23:46:39 2018

@author: fubao
"""




'''
Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions.

Each function has a unique id, start from 0 to n-1. A function may be called recursively or by another function.

A log is a string has this format : function_id:start_or_end:timestamp. For example, "0:start:0" means function 0 starts from the very beginning of time 0. "0:end:0" means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions should not be considered as this function's exclusive time. You should return the exclusive time of each function sorted by their function id.

Example 1:
Input:
n = 2
logs = 
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
Output:[3, 4]
Explanation:
Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1. 
Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time. 
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.
Note:
Input logs will be sorted by timestamp, NOT log id.
Your output should be sorted by function id, which means the 0th element of your output corresponds to the exclusive time of function 0.
Two functions won't start or end at the same time.
Functions could be called recursively, and will always end.
1 <= n <= 100
'''


'''
e.g.


1
["0:start:0",
 "0:start:2",
 "0:end:5",
 "0:start:6",
 "0:end:6",
 "0:end:7"]


2
["0:start:0",
 "0:start:2",
 "0:end:5",
 "1:start:6",
 "1:end:6",
 "0:end:7"]

2
["0:start:0",
 "0:start:2",
 "0:end:5",
 "1:start:7",
 "1:end:7",
 "0:end:8"]
'''


def exclusiveTime(n, logs):
    """
    :type n: int
    :type logs: List[str]
    :rtype: List[int]
    """
    '''
    #Failed 1st naive way: iterate the logs list, parse the id and timeStamp,
    #record the function Id, and timeStamp of current visit and previous one.
    place into the hashmap dic,  key is the function Id, value is the timeStamp list.
    compare current visited func Id and previous func Id, and set the previous xx = current
    if the same, keep adding the dic, if not the same, if current starts, then set previous func end, and put the (current timestamp-1) into dic of previous ID; if current end, then no and start and end timestamp the same (or no adding)
    '''
    '''
    if logs is None or len(logs) == 0:
        return None
    
    f1 = logs[0]
    info = f1.split(':')
    pretid = info[0]
    prelabel = info[1]
    pretime = info[2]
    dicTask = defaultdict(list)
    dicTask[pretid].append(int(pretime))
    for i in range(1, len(logs)):
        currentInfo = logs[i].split(':')
        curtid = currentInfo[0]
        curlabel = currentInfo[1]
        curtime = currentInfo[2]
        
        if curtid != pretid and curlabel == 'start' and prelabel == 'start':
            dicTask[pretid].append(int(curtime)-1)
        elif curtid != pretid and curlabel == 'start' and prelabel == 'end':
            dicTask[pretid].append(int(pretime)+1)
            dicTask[pretid].append(int(curtime)-1)

        elif curtid != pretid and curlabel == 'end':
            dicTask[curtid].append(int(pretime)+1)
        
        if curtid == pretid and curlabel == 'start' and prelabel == 'start':
            dicTask[curtid].append(int(curtime)-1)
        #    dicTask[curtid].append(int(curtime))
        if curtid == pretid and curlabel == 'end' and prelabel == 'end':
            dicTask[curtid].append(int(pretime)+1)
        dicTask[curtid].append(int(curtime))


        #dicTask[curtid].append(int(curtime))
        
        pretid = curtid
        pretime = curtime
        prelabel = curlabel
        
    ans = []
    for tk in sorted(dicTask):
        val = dicTask[tk]
        ans.append(sum([(val[i+1] - val[i] +1) for i in range(0, len(val)-1, 2)]))
        
    #print ("dicTask: ", dicTask)
    
    return ans
    '''
    
    '''
    # 2nd failed use stack; if 'start', put in the stack, if 'end', pop from stack, calculate the time difference; but have to deduct the intermediate task's time used. So keep record the 
    stk = []
    ansLst = [-1]*n
    intermedDict = defaultdict(list)
    for i, lg in enumerate(logs):
        info = lg.split(":")
        tid = int(info[0])
        label = info[1]
        time = int(info[2])
        
        if label == 'start':
            #put in the stack
            #print ("tid: ", i, tid, stk[-1][0],stk)
            if i != 0 and len(stk) != 0 and stk[-1][0] != tid:
                intermedDict[stk[-1][0]].append(tid)
            stk.append((tid, label, time))

        elif label == 'end':
            #pop
            elePop = stk.pop(-1)
            if ansLst[tid] == -1:       # first time encountered
                ansLst[tid] = time - elePop[2] + 1 - sum(ansLst[i] for i in  intermedDict[tid])
            else:
                if intermedDict[tid] == []:
                    ansLst[tid] = time - elePop[2] + 1 
                else:
                    ansLst[tid] = time - elePop[2] + 1  + ansLst[i] - sum(ansLst[i] for i in  intermedDict[tid])
            if len(stk) != 0 and stk[-1][0] != tid and tid in intermedDict:
                del intermedDict[tid]
    print ("intermedDict: ", intermedDict)
    return ansLst
    '''
    
    # SUCCESS 3rd try; use stack again,  if 'start', put in the stack, if 'end', pop from stack; keep it out from the stack. But we need to keep the pre record's time
    
    ans = [0] * n  #defaultdict(int)
    stk = []     # stack
    for i, lg in enumerate(logs):
        info = lg.split(":")
        tid = int(info[0])
        label = info[1]
        time = int(info[2])
        if i == 0:
            stk.append((tid, label, time))
            prev = time
        else:
            if label == 'start':
                if len(stk) != 0:
                    ans[stk[-1][0]] += time - prev
                stk.append((tid, label, time))
                prev = time
            elif label == 'end':
                stk.pop(-1)
                ans[tid] += time - prev + 1
                prev = time + 1
            
    #print ("ans: ", ans)
    return ans              
    
    
n = 2 
logs = ["0:start:0",
 "0:start:2",
 "0:end:5",
 "1:start:7",
 "1:end:7",
 "0:end:8"]        
logs = ["0:start:0",
 "0:start:2",
 "0:end:5",
 "1:start:6",
 "1:end:6",
 "0:end:7"]   

n = 1
logs = ["0:start:0",
 "0:start:2",
 "0:end:5",
 "0:start:6",
 "0:end:6",
 "0:end:7"]

exclusiveTime(n, logs)





