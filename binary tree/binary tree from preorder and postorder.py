# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, pre, post):
        if post:
            if len(post) == 1:
                return TreeNode(pre.pop(0))
            root_val = pre.pop(0)
            ind = post.index(pre[0])
            root = TreeNode(root_val)
            root.left = self.construct(pre, post[:ind + 1])
            root.right = self.construct(pre, post[ind + 1:-1])
            return root

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.construct(preorder, postorder)
