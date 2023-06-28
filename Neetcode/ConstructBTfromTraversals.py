# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        h = TreeNode(preorder[0])
        head = h
        nodeindex = dict()
        for i in range(len(inorder)):
            nodeindex[inorder[i]] = i
        headindex = nodeindex[preorder[0]]
        i = 1
        while i < len(preorder):
            if nodeindex[preorder[i]] < headindex:
                if head.left is None:
                    head.left = TreeNode(preorder[i])
                    i += 1
                else:
                    head = head.left
                    headindex = nodeindex[head.val]
                    continue
            else:
                if head.right is None:
                    head.right = TreeNode(preorder[i])
                    i += 1
                else:
                    head = head.right
                    headindex = nodeindex[head.val]
                    continue
            head = h
            headindex = nodeindex[head.val]
        return h
