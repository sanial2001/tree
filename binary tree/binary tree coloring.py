# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def dfs(self, node, flag):
        if not node:
            return
        self.graph[node.val] += 1
        self.color[flag] += 1
        self.dfs(node.left, not flag)
        self.dfs(node.right, not flag)

    def solve(self, root):
        self.graph = collections.defaultdict(int)
        self.color = collections.defaultdict(int)
        self.dfs(root, True)
        # print(self.graph.values(), self.color.values())
        return True if set(self.graph.values()) == set(self.color.values()) else False
