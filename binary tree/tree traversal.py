# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, moves, i, prev):
        if not node or i == len(moves):
            if prev != "UP": self.stack.append(node)
            return
        if prev != "UP": self.stack.append(node)
        if moves[i] == "LEFT":
            # print(self.stack[-1].val)
            self.dfs(node.left, moves, i + 1, "LEFT")
        if moves[i] == "RIGHT":
            self.dfs(node.right, moves, i + 1, "RIGHT")
        if moves[i] == "UP":
            self.stack.pop()
            i += 1
            while i < len(moves) and moves[i] == "UP":
                self.stack.pop()
                i += 1
            self.dfs(self.stack[-1], moves, i, "UP")

    def solve(self, root, moves):
        self.stack = []
        self.dfs(root, moves, 0, "")
        return self.stack[-1].val
