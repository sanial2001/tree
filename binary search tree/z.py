def solve(x, y, z):
    out = z.copy()
    visit = set()
    while z:
        val = z.pop(0)
        if 2 * val <= x and 2 * val not in visit and 2 * val + 1 not in visit:
            out.append(2 * val)
            z.append(2 * val)
            visit.add(2 * val)
            out.append(2 * val + 1)
            z.append(2 * val + 1)
            visit.add(2 * val + 1)

    res = []
    for i in range(1, x + 1):
        if i not in out:
            res.append(i)

    return [0] if not res else res


if __name__ == "__main__":
    print(solve(7, 1, [1]))
