# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        return 1 + self.dfs(node.left) + self.dfs(node.right)

    def bfs(self, root):
        if not root:
            return 0
        q = [root]
        ans = 0
        while q:
            node = q.pop(0)
            ans += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans

    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
        # return self.bfs(root)
