# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = list()
        def lrrt(root):
            if root is None:
                return None
            lrrt(root.left)
            nodes.append(root.val)
            lrrt(root.right)
        lrrt(root)
        return nodes[k-1]
