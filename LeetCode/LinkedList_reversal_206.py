class LinekedList:
    def __init__(self, val, nextref=None):
        self.val = val
        self.next = nextref

    # def reverse_list(self, head):
    #         curr = head
    #         prev = None
    #
    #         while curr:
    #             temp = curr.next
    #             curr.next = prev
    #             prev = curr
    #             curr = temp
    #
    #         return prev

    def reverse_list(self, Head):

        prev = None

        while Head:
            print(Head.val)
            temp = Head.next
            Head.next = prev
            prev = Head
            Head = temp

        return prev
    # TC  - O(n) SC : O(1)

    def display(self):
        elements = []
        while self:
            elements.append(str(self.val))
            self = self.next
        print("->".join(elements))


A = LinekedList(1)
B = LinekedList(2)
C = LinekedList(3)
D = LinekedList(4)
E = LinekedList(5)
A.next = B
B.next = C
C.next = D
D.next = E
print(A.display())
A.reverse_list(A)
print(A.display())


# Submitted solution
# class Solution:
#
#
# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#     curr = head
#     prev = None
#
#     while curr:
#         temp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = temp
#
#     return prev


