# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        while head1 is not None and head2 is not None:
            # print(head1.val, list1.val, list2.val)
            if head1.val >= head2.val:
                head1, head2 = head2, head1
            if head1.next and head1.next.val < head2.val:
                head1 = head1.next
            elif head1.next is not None:
                temp = head1.next
                head1.next = head2
                head1 = temp
            elif head1.next is None and head2 is not None:
                head1.next = head2
                break
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val >= list2.val:
            return list2
        else:
            return list1
