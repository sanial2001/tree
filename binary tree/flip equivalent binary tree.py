# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        # print(node1.val, node2.val)
        if node1.val != node2.val:
            return False
        l1, l2 = self.dfs(node1.left, node2.left), self.dfs(node1.left, node2.right)
        r1, r2 = self.dfs(node1.right, node2.right), self.dfs(node1.right, node2.left)
        return (l1 or l2) and (r1 or r2)

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1, root2)
