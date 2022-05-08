# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return
        self.d[node.val] = self.d.get(node.val, 0) + 1
        self.dfs(node.left)
        self.dfs(node.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.d = {}
        self.dfs(root)
        ans = []
        max_val = max(self.d.values())
        for key in self.d:
            if self.d[key] == max_val:
                ans.append(key)
        return ans
