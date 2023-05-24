# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeset = set()
        if head == None:
            return False
        while head:
            if head in nodeset:
                return True
            else:
                nodeset.add(head)
                head = head.next
        return False
