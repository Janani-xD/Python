#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:40:11 2024

@author: janani
"""

def arrange_in_descending(List):
    return List

def linear_search(List, Query):
    """
    We are about to write the most basic algorithm available in programming to select a query from a list of elements.
    Inputs : List, Query
    Output : Position
    Fristly arrange the elements in descending order
    worst case scenario would be the element at the end of the list.
    good case scenario would be the first element in the list
    other cases could be 
        an empty list
        a non existing query in the list
        picking a element before n/2
        picking a element after n/2
    """
    ListLen = len(List)
    QueryFound = False
    pos = 0
    ArrangedList = arrange_in_descending(List)
    while pos < ListLen:
        if ArrangedList[pos] == Query:
            QueryFound = True
            return pos
        else:
            pos+=1
    if QueryFound == True:
        return pos
    else: 
        return -1
Return = linear_search([21,111,100,2,10,5], 5)
print(f'Position of {10000} : {Return}')
