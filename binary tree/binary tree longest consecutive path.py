'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    # your task is to complete this function
    # function should print the top view of the binary tree
    # Note: You aren't required to print a new line after every test case
    def dfs(self, node):
        if not node:
            return 0
        res = 1
        l, r = self.dfs(node.left), self.dfs(node.right)
        if node.left and node.left.data == node.data + 1:
            res = max(res, l + 1)
        if node.right and node.right.data == node.data + 1:
            res = max(res, r + 1)
        self.ans = max(self.ans, res)
        return res

    def longestConsecutive(self, root):
        # Code here
        self.ans = 0
        self.dfs(root)
        return -1 if self.ans == 1 else self.ans


# {
# Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        print(Solution().longestConsecutive(root))

# } Driver Code Ends
