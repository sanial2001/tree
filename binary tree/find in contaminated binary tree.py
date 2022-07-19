# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.d = set()
        self.d.add(0)
        q = [root]
        while q:
            num = len(q)
            for i in range(num):
                node = q.pop(0)
                if node.left:
                    node.left.val = 2 * node.val + 1
                    self.d.add(node.left.val)
                    q.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    self.d.add(node.right.val)
                    q.append(node.right)
        # self.dfs(root)

    def find(self, target: int) -> bool:
        return True if target in self.d else False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
