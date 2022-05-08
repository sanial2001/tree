# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, path, sums, k):
        if not node:
            return
        if not node.left and not node.right:
            path.append(node.val)
            sums += node.val
            if sums == k:
                self.ans.append(path)
            return
        self.dfs(node.left, path + [node.val], sums + node.val, k)
        self.dfs(node.right, path + [node.val], sums + node.val, k)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        self.dfs(root, [], 0, targetSum)
        return self.ans
