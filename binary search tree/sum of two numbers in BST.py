# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node1, node2, target):
        if not node1 or not node2:
            return False
        sums = node1.val + node2.val
        if sums == target:
            return True
        if sums > target:
            return self.dfs(node1.left, node2, target) or self.dfs(node1, node2.left, target)
        else:
            return self.dfs(node1.right, node2, target) or self.dfs(node1, node2.right, target)

    def solve(self, a, b, target):
        return self.dfs(a, b, target)
