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
        if node1.val != node2.val:
            return False
        left, right = self.dfs(node1.left, node2.left), self.dfs(node1.right, node2.right)
        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = [root]
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                if node.val == subRoot.val:
                    if self.dfs(node, subRoot):
                        return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False
