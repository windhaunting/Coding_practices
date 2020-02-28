'''
from collections import defaultdict


'''
'''
idea 1:  has bugs in the code
time complexity o(1), space complexiy o(capacity)
(1) we use dictionary to store the key and value 
the dictionary number is limited
  ;  
  To find the least recently key to replace: we do the three things
  (2) we store each key's secondly recently key as a dictionary, 
  (3) store the least recent key and most recent key 
  we need to update these 3 variables when we call the function "put"
  
''' 
'''


class LRUCache:

    def __init__(self, capacity: int):
        
        self.dict_cache = defaultdict(int)
        self.least_recent_key = None
        self.most_recent_key = None
        
        self.dict_upper_recent = defaultdict(int)
        self.dict_lower_recent = defaultdict(int)
        
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        
              
        if key not in self.dict_cache:
            return -1
        else:
            if key == self.least_recent_key:
                self.least_recent_key = self.dict_upper_recent[self.least_recent_key]
                self.dict_upper_recent[self.most_recent_key]  = key
                self.most_recent_key = key
                self.dict_upper_recent[self.most_recent_key]  = None
            elif key != self.most_recent_key:
                self.dict_upper_recent[self.most_recent_key]  = key
                self.most_recent_key = key
                self.dict_upper_recent[self.most_recent_key]  = None

                last_key= self.dict_lower_recent[key] 

                self.dict_upper_recent[last_key] =  self.dict_upper_recent[key]
                self.dict_lower_recent[self.dict_upper_recent[key]] = last_key
                
            return self.dict_cache[key]
            
    def put(self, key: int, value: int) -> None:
        
        
        if len(self.dict_cache) <  self.capacity:
            self.dict_cache[key] = value
            
            if  self.least_recent_key is None:
                self.least_recent_key = key
                self.most_recent_key = key
                
            if self.most_recent_key is not None:
                self.dict_upper_recent[self.most_recent_key] = key
                self.most_recent_key = key

                self.dict_lower_recent[key] = self.most_recent_key
                
            self.dict_upper_recent[self.most_recent_key] = self.most_recent_key
            
        else:
            # find the least recently key
            if key not in self.dict_cache:
                del self.dict_cache[self.least_recent_key]
                
            self.dict_cache[key] = value
            
            self.least_recent_key = self.dict_upper_recent[self.least_recent_key]
            
            self.most_recent_key = key
            self.dict_upper_recent[self.most_recent_key] = self.most_recent_key
            
            print ("self.least_recent_key", key, self.least_recent_key, self.dict_cache)

        
         
            print ("self,dict_cache", len(self.dict_cache), self.dict_cache)

    '''
        
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)

    #bugs not processed 
    
    
    # look at the reference  reference: https://www.programcreek.com/2013/03/leetcode-lru-cache-java/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = None
        self.tail = None
        self.dict_cache = {}      # store the Node as the value
        
    def get(self, key: int) -> int:     
        if key not in self.dict_cache:
            return -1
        
        #move to tail
        #remove the node
        t = self.dict_cache[key]
        self.removeNode(t)
        self.appendNode(t)
        
        return t.val
    
    def put(self, key: int, value: int) -> None:
        
        if key in self.dict_cache:
            t = self.dict_cache[key]
            t.val = value
            # move to tail
            self.removeNode(t)
            self.appendNode(t)
        else:
            if self.cap <= len(self.dict_cache):
                # remove head
                del self.dict_cache[self.head.key]
                self.removeNode(self.head)

            # add to tail
            t = Node(key, value)
            self.appendNode(t)
            self.dict_cache[key] = t # store the node
        
        
    def removeNode(self, nd) -> None:
        if nd.prev is None:
            self.head = nd.next
        else:
            nd.prev.next = nd.next

        if nd.next is None:
            self.tail = nd.prev
        else:
            nd.next.prev = nd.prev
            
    def appendNode(self, nd) -> None:

        if self.tail is not None:
            self.tail.next = nd

        nd.prev = self.tail
        nd.next = None
        self.tail = nd

        if self.head is None:
            self.head = self.tail


            
        
            