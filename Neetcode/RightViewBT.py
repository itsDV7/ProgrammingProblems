# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        dq = deque()
        dq.append(root)
        while dq:
            ans.append(dq[-1].val)
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
        return ans
