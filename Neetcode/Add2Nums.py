# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        carry = 0
        head = ListNode(-1)
        start = head

        while h1 is not None and h2 is not None:
            if carry:
                add = h1.val + h2.val + 1
            else:
                add = h1.val + h2.val
            carry = add//10
            head.next = ListNode(add%10)
            head = head.next
            h1 = h1.next
            h2 = h2.next

        if h1 is not None:
            head.next = h1
            head = head.next
        elif h2 is not None:
            head.next = h2
            head = head.next
        else:
            if carry:
                head.next = ListNode(1)
            return start.next


        while head is not None and carry:
            add = head.val + carry
            carry = add//10
            head.val = add%10
            temp = head
            head = head.next
        
        if carry:
            temp.next = ListNode(1)
        
        return start.next
