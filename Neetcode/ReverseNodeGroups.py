# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None or k == 1:
            return head
        
        h = head
        count = 0
        while h:
            count += 1
            h = h.next

        divs = count // k

        if count == k:
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

        lastnode = None
        back = head
        front = head.next
        for i in range(divs):
            back.next = None
            startnode = back
            for j in range(k-1):
                temp = front.next
                front.next = back
                back = front
                front = temp
            if lastnode is None:
                returnnode = back
            else:
                lastnode.next = back
            lastnode = startnode
            startnode.next = front
            back = front
            if back is not None:
                front = back.next
                
        return returnnode
