# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, i, p):
        if i:
            rootval = p.pop()
            # print(rootval)
            rootind = i.index(rootval)
            root = TreeNode(rootval)
            root.right = self.construct(i[rootind + 1:], p)
            root.left = self.construct(i[:rootind], p)
            return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.construct(inorder, postorder)
