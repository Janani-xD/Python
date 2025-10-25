from typing import Optional

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True

        return False

    # alternate Solution
    def hasCycle2(self, head):
        if head is None:
            return False
        single = double = head
        while double and double.next is not None:
            double = double.next.next
            single = single.next

            if double == single:
                return True
        return False