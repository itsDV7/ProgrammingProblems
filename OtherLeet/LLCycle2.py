# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow, fast = head, head

        if head is None:
            return None

        while True:
            slow = slow.next
            if slow is None:
                return None
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            if fast is None:
                return None
            if slow == fast:
                break

        loop = head

        if loop == slow:
            return slow

        while True:
            loop = loop.next
            slow = slow.next
            if loop == slow:
                return slow

        return None
