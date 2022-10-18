def solve(n, nums):
    g = {i + 1: [] for i in range(n)}
    for i, val in enumerate(nums):
        g[val].append(i + 2)

    d = {i + 1: 1 for i in range(n)}

    def dfs(node):
        for nei in g[node]:
            dfs(nei)
            d[node] += d[nei]

    dfs(1)
    res = []
    for key in d:
        res.append(d[key] - 1)
    return res


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(*solve(n, nums))


if __name__ == "__main__":
    main()
