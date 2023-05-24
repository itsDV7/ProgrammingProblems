# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        back = head
        front = head.next
        if front is None:
            return back
        back.next = None
        while front.next is not None:
            temp = front.next
            front.next = back
            back = front
            front = temp
        front.next = back
        return front
