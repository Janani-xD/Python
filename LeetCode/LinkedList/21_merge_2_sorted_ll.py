# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        d = curr
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next

            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        curr.next = list1 if list1 else list2
        return d.next
    # ALTERNATIVELY
    def mergeTwoLists2(self, list1, list2)
        head = ListNodde(None)
        curr = head
        while list1 or list2:
            if list1 is None
                curr.next = list2
                return head.next
            if list2 is None:
                curr.next = list1
                return head.next
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        return head.next

        :