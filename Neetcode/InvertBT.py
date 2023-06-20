# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        root.left, root.right = root.right, root.left
        if root.right is not None:
            self.invertTree(root.right)
        if root.left is not None:
            self.invertTree(root.left)
        return root
