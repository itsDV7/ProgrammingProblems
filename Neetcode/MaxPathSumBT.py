# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            pathsum = root.val + max(left, right, 0)
            print(root.val, pathsum)
            res[0] = max([res[0], pathsum, root.val+left+right, root.val])
            return pathsum
        dfs(root)
        return res[0]
