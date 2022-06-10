# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return [float("inf"), float("-inf"), True, None, 0]
        if not node.left and not node.right:
            return [node.val, node.val, True, node, 1]
        l, r = self.dfs(node.left), self.dfs(node.right)
        node_min = min(l[0], r[0], node.val)
        node_max = max(l[1], r[1], node.val)
        if l[2] and r[2] and l[1] < node.val < r[0]:
            return [node_min, node_max, True, node, l[4] + r[4] + 1]
        elif l[4] > r[4]:
            return [node_min, node_max, False, l[3], l[4]]
        else:
            return [node_min, node_max, False, r[3], r[4]]

    def solve(self, root):
        return self.dfs(root)[3]
