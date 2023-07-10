# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        minheight = [float('inf')]
        def dfs(root, height):
            if root.left is None and root.right is None:
                minheight[0] = min(minheight[0], height)
                return
            if root.left is not None:
                dfs(root.left, height+1)
            if root.right is not None:
                dfs(root.right, height+1)
        dfs(root, 1)
        return minheight[0]
