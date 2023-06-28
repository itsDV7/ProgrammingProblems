# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        smallnode = []
        def lrrt(root):
            if root is None:
                return None
            lrrt(root.left)
            if smallnode:
                if smallnode[0][0] < root.val:
                    smallnode[0] = (root.val, smallnode[0][1] and True)
                else:
                    smallnode[0] = (root.val, False)
            else:
                smallnode.append((root.val, True))
            print(smallnode[0])
            lrrt(root.right)
        lrrt(root)
        return smallnode[0][1]
