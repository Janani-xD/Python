"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
Input: head = [1,2,2,1]
Output: true
Input: head = [1,2]
Output: false
"""
from typing import Optional

from pandas.tseries.holiday import previous_friday

from DSA.LinkedList.DoublyLinkedList import head1


# Definition for singly-linked list.
class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: # if the ll has only one node its still a palindrome
            return True

       #step one is to find the mid point of the singly - linked list ( using fast and slow pointer technique) works
       # for both odd and even length linked list
        fast = slow = head
        while fast and fast.next:
           fast = fast.next.next
           slow = slow.next

       # step 2 is to reverse the linked list from the mid()
        prev = None  # aim is the point to None when the LL  is traversed from the end after mid point it should point
                    # to none such that the iteration will stop
        curr = slow # indicates the mid point of linked list
        while curr:
            tmp = curr.next  # tmp stores mid.next
            curr.next = prev # mid.next is None
            prev = curr # prev is mid node
            curr = tmp # curr is mid.next
        # after the loop ends prev will become none and the elements are reversed

        h1 = head #points to first node
        h2 = prev #points to last node
        while h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True





