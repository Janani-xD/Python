# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        if len(l1) >= len(l2):
            length = len(l2)
            for i in range(length):
                l1[i] = l1[i] + l2[i]
            return l1
        elif len(l2) >= len(l1):
            length = len(l1)
            for i in range(length):
                l2[i] = l1[i] + l2[i]
            return l2
        else:
            for i in range(len(l1)):
                l1[i] = l1[i] + l2[i]
            return l1


my_obj = Solution()
print(my_obj.addTwoNumbers([1,2,4,5],[1,2,3,23,5]))