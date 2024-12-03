#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:40:11 2024

@author: janani
"""

""" Insertion Sort
    It utilizes the temp variable concept to arracnge the elements in ascending order
    Starting from the second element, Stores the smaller value in temp and re-positions the elements on the left by right shifting
    
    Pseudo code. 
        select second element
        if element greater that previous element -> do nothing
        else element it smaller that previous element store in temp move previous element to current element and check all the previous element until 0 and finally place the temp element in appropriate index.
        
        
"""


    
def insertion_sort(Array):
    for step in range(1, len(Array)):
        key = Array[step]
        j = step - 1
        while j >= 0 and key < Array[j]:
            Array[j+1] = Array[j]
            j = j - 1
            Array[j+1] = key   
            
            
            
start = time.time()
Array = [6,1,7,4,2,9,8,5,3]
insertion_sort(Array)
print("Sorted Array : ", Array)
end = time.time()
Time = (end - start) * 10 ** 3
print(f' Execution Time for insertion sort : {Time} ms')

