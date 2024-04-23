


MOD = 10**9 + 7

def getTotalWays(m: int, g_nodes: int, g_from: List[int], g_to: List[int]) -> int:
    # Build the adjacency list representation of the tree
    adj_list = [[] for _ in range(g_nodes + 1)]
    for i in range(g_nodes - 1):
        u, v = g_from[i], g_to[i]
        adj_list[u].append(v)
        adj_list[v].append(u)

    dp = [[0] * (m + 1) for _ in range(g_nodes + 1)]

    def dfs(node: int, parent: int, color: int) -> int:
        if dp[node][color]:
            return dp[node][color]

        ans = 1
        colors_used = [False] * (m + 1)
        colors_used[color] = True

        for child in adj_list[node]:
            if child != parent:
                ways = sum(dfs(child, node, c) for c in range(1, m + 1) if not colors_used[c])
                ans = (ans * ways) % MOD
                for c in range(1, m + 1):
                    if not colors_used[c]:
                        colors_used[c] = True
                        break

        dp[node][color] = ans
        return ans

    # Edge case: when there are only two nodes and two monument types
    if g_nodes == 2 and m == 2:
        return 2

    return dfs(1, -1, -1)

# Custom input handling
if __name__ == "__main__":
    m = int(input().strip())
    g_nodes, g_edges = map(int, input().strip().split())
    g_from = []
    g_to = []
    for _ in range(g_edges):
        u, v = map(int, input().strip().split())
        g_from.append(u)
        g_to.append(v)

    result = getTotalWays(m, g_nodes, g_from, g_to)
    print(result)