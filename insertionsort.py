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

def swap_insertion_elems(Array, i):
    temp = Array [i]
    print("temp : " ,temp)
    while i >= 0:
        if Array[i-1] > Array[i]:
            Array[i] = Array[i-1]
        else:
            Array[i-1] = temp
        i-=1
    return Array
    
    
def insertion_sort():
    Array = [6,1,7,4,2,9,8,5,3]
    for i in range(1, len(Array)):
        print("i : " , i )
        if Array[i] < Array [i - 1]:
            swap_insertion_elems(Array, i)
    return Array        
            
            
            
start = time.time()
print("Sorted Array : ",  insertion_sort())
end = time.time()
Time = (end - start) * 10 ** 3
print(f' Execution Time for insertion sort : {Time} ms')

