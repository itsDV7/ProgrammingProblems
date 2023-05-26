# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            return None
        elif head.next is None:
            return head
        nodecount = 0
        h = head
        while h is not None:
            nodecount += 1
            h = h.next
        if nodecount == n:
            return head.next
        delnode = nodecount - n
        h = head
        i = 0
        while h is not None and i < delnode:
            if i+1 == delnode:
                h.next = h.next.next
            h = h.next
            i += 1
        return head
