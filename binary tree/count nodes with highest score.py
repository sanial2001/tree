class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        g = {i: [] for i in range(n)}
        for u, v in enumerate(parents):
            if v != -1:
                g[v].append(u)
        # print(g.items())

        d = {i: 1 for i in range(n)}

        def dfs(node):
            for nei in g[node]:
                dfs(nei)
                d[node] += d[nei]

        dfs(0)
        # print(d.items())
        res = []
        for node in range(n):
            if d[node] == 1:
                res.append(n - 1)
            else:
                cnt = 1
                for nei in g[node]:
                    cnt *= d[nei]
                if parents[node] != -1:
                    cnt *= (n - d[node])
                res.append(cnt)
            # print(res)

        return res.count(max(res))
