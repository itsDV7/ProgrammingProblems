# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        pq = PriorityQueue()
        knodes = len(lists)
        if knodes < 2:
            return lists[0]

        nodedict = dict()

        for k in range(knodes):
            if lists[k]:
                nodedict[k] = lists[k]
                pq.put((lists[k].val, k))

        dummy = ListNode(0)
        returnnode = dummy

        while not pq.empty():
            smallest, key = pq.get()
            node = nodedict[key]
            dummy.next = node
            dummy = dummy.next
            if nodedict[key].next is not None:
                nodedict[key] = nodedict[key].next
                pq.put((nodedict[key].val, key))

        return returnnode.next
