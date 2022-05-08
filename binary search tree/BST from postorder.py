# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, inorder, preorder):
        if inorder:
            root_val = preorder.pop()
            root_ind = inorder.index(root_val)
            root = TreeNode(root_val)
            root.right = self.construct(inorder[root_ind + 1:], preorder)
            root.left = self.construct(inorder[:root_ind], preorder)
            return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        return self.construct(inorder, preorder)
