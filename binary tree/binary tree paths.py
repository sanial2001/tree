# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            path = path + "->" + str(node.val)
            path = path[2:]
            self.ans.append(path)
            return
        self.dfs(node.left, path + "->" + str(node.val))
        self.dfs(node.right, path + "->" + str(node.val))

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.dfs(root, "")
        return self.ans
