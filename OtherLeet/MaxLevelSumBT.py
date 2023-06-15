# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        nodes = deque()
        nodes.append(root)
        maxsum = root.val
        level = 1
        maxlevel = 1
        while nodes:
            nodecount = 0
            currsum = 0
            for n in nodes:
                nodecount += 1
                currsum += n.val
            print(level, currsum)
            if currsum > maxsum:
                maxlevel = level
                maxsum = currsum
            for _ in range(nodecount):
                n = nodes.popleft()
                if n.left is not None:
                    nodes.append(n.left)
                if n.right is not None:
                    nodes.append(n.right)
            level += 1
        print(maxsum)
        return maxlevel
