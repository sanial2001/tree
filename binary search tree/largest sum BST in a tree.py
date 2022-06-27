# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return [float("inf"), float("-inf"), True, None, 0, 0]
        if not node.left and not node.right:
            return [node.val, node.val, True, node, 1, node.val]
        l, r = self.dfs(node.left), self.dfs(node.right)
        low = min(l[0], r[0], node.val)
        hi = max(l[1], r[1], node.val)
        if l[2] and r[2] and l[1] < node.val < r[0]:
            return [low, hi, True, node, l[4] + r[4] + 1, l[5] + r[5] + node.val]
        elif l[4] > r[4]:
            return [low, hi, False, l[3], l[4], l[5]]
        else:
            return [low, hi, False, r[3], r[4], r[5]]

    def solve(self, root):
        return self.dfs(root)[5]
