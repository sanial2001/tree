# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, graph, node, parent):
        if parent:
            graph[node].append(parent)
        if node.left:
            graph[node].append(node.left)
            self.dfs(graph, node.left, node)
        if node.right:
            graph[node].append(node.right)
            self.dfs(graph, node.right, node)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        self.dfs(graph, root, None)

        q = [(target, 0)]
        ans = []
        visit = {target}
        while q:
            node, dist = q.pop(0)
            # print(node.val)
            if dist > k:
                break
            if k == dist:
                ans.append(node.val)
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    q.append((nei, dist + 1))
        return ans
