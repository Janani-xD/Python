#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:40:11 2024

@author: janani
"""

""" BUBBLE SORT 
    Takes element by element and traverses through the rest of the array to arrange the element in ascending order
    Basically it should hold two loops one to pick each element and the other to traverse through the array
    It natuarlly becomes a slow performing algorithm
    
    Time complexity : 
        Best case scenario : O(n)
        worst case scenario : O(n^2)
        Avg case scenario : O(n^2)
    Space Complexity : O(1)
"""

def swap_elements(Array, i):
    temp = Array[i]
    Array[i] = Array[i + 1]
    Array[i+1] = temp
    return Array

def bubble_sort(Array):
    # Array = [10,2,5,3,1]
    ArrayLength = len(Array)
    for element in Array: # loop to iterate through every element
        i=0
        for j in range(i, ArrayLength - 1): # loop to iterate through the array for every chosen element
            if Array[i] > Array[i+1]:
                swap_elements(Array,i)
            i+=1
    return Array

start = time.time()   
print("Sorted Array : ",  bubble_sort([100,25,1,10]))
end = time.time()
Time = (end - start) * 10 ** 3
print(f' Execution Time for bubble sort : {Time} ms')
