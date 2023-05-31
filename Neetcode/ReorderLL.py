# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # tail = head
        # while tail.next is not None:
        #     tail = tail.next
        
        # h1 = head
        # c = head

        # while h1.next != tail and h1.next is not None:
        #     while c.next != tail:
        #         c = c.next
        #     temp = h1.next
        #     h1.next = tail
        #     tail.next = temp
        #     c.next = None
        #     h1 = temp
        #     tail = c
        #     c = h1

        if head.next is None:
            return head
    
        nodearr = list()
        h = head
        while h is not None:
            nodearr.append(h)
            h = h.next

        for i in range(len(nodearr)//2):
            if i:
                nodearr[len(nodearr) - i].next = nodearr[i]
                nodearr[i].next = nodearr[len(nodearr) - i - 1]
                nodearr[len(nodearr) - i - 1].next = None
            else:
                nodearr[i].next = nodearr[len(nodearr) - i - 1]
                nodearr[len(nodearr) - i - 1].next = None

        if len(nodearr) % 2:
            nodearr[len(nodearr)//2 + 1].next = nodearr[len(nodearr)//2]
            nodearr[len(nodearr)//2].next = None

        return head

# Slow Fast pointer approach O(n) time O(1) space
#         slow = head
#         fast = head.next

#         while fast is not None and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next

#         prev = None
#         nxt = slow.next
#         slow.next = None

#         while nxt is not None:
#             temp = nxt.next
#             nxt.next = prev
#             prev = nxt
#             nxt = temp

#         while prev is not None:
#             headnext = head.next
#             prevnext = prev.next
#             head.next = prev
#             prev.next = headnext
#             head = headnext
#             prev = prevnext

#         if head is not None:
#             prevnext = head

#         return head
