"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head.next is None:
            val = head.val
            if head.random is None:
                return Node(val, None, None)
            else:
                newnode = Node(val)
                newnode.next = None
                newnode.random = newnode
                return newnode
        nodedict = dict()
        newhead = Node(head.val)
        nodedict[head] = newhead
        while head is not None:
            if head in nodedict:
                newnode = nodedict[head]
            else:
                newnode = Node(head.val)
                nodedict[head] = newnode
            if head.next in nodedict:
                newnode.next = nodedict[head.next]
            else:
                if head.next is None:
                    newnode.next = None
                else:
                    nextnode = Node(head.next.val)
                    newnode.next = nextnode
                    nodedict[head.next] = nextnode
            if head.random in nodedict:
                newnode.random = nodedict[head.random]
            else:
                if head.random is None:
                    newnode.random = None
                else:
                    randomnode = Node(head.random.val)
                    newnode.random = randomnode
                    nodedict[head.random] = randomnode
            head = head.next
        return newhead
