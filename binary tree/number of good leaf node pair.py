# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return [0]
        if not node.left and not node.right:
            return [1]
        left, right = self.dfs(node.left), self.dfs(node.right)
        left, right = [val for val in left if val != 0], [val for val in right if val != 0]
        # print(left, right)
        for l in left:
            for r in right:
                if l + r <= self.d:
                    self.ans += 1
        left, right = [i + 1 for i in left], [i + 1 for i in right]
        return left + right

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans, self.d = 0, distance
        sums = self.dfs(root)
        return self.ans
