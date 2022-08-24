# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, d):
        if not node:
            return 'N'
        l, r = self.dfs(node.left, d), self.dfs(node.right, d)
        path = str(node.val) + '-' + l + '-' + r
        # print(path)
        if path in d:
            d[path] += 1
            if d[path] == 2:
                self.res.append(node)
        else:
            d[path] = 1
        return path

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.res = []
        self.dfs(root, dict())
        return self.res
