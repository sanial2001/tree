# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return []
        left, right = self.dfs(node.left), self.dfs(node.right)
        return left + [node.val] + right

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        in_1 = self.dfs(root1)
        in_2 = self.dfs(root2)
        return sorted(in_1 + in_2)
