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
