import math
import os
import random
import re
import sys

class Node :
    def __init__(self, value):
        self.dataval = value
        self.nextval = None

class SLinkedList :
        def __init__(self):
            self.headval = None
        
        def Display(self):
            val = self.headval
            while(val != None):
                print(str(val.dataval)+ "->", end=" ")
                val = val.nextval
        
        def InsertAtStart(self, data):
            node = Node(data)
            node.nextval = self.headval
            self.headval = node

        def Remove(self,key):
            
            if(self.headval.dataval == key):
                self.headval = self.headval.nextval
                return
            
            head = self.headval
            prev = None
            while(head is not None):
                if(head.dataval == key):
                    break
                prev = head
                head = head.nextval
            
            if(prev is not None and head is not None):
                prev.nextval = head.nextval

sList = SLinkedList()

for x in range(10):
    sList.InsertAtStart(x)
sList.Display()
sList.Remove(510)
sList.Display()
