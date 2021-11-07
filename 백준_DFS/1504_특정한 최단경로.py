import heapq
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = sys.maxsize

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

v1, v2 = map(int, input().split())


def dfs(node):
    dist = [inf] * (N+1)
    q = []
    heappush(q, [0, node])
    dist[node] = 0
    while q:
        cost, node = heappop(q)
        for n_cost, n_node in graph[node]:
            total_cost = cost + n_cost
            if dist[n_node] > total_cost:
                dist[n_node] = total_cost
                heappush(q, [total_cost, n_node])

    return dist

a = dfs(1)
b = dfs(v1)
c = dfs(v2)
# 1.  1 -> v1 -> v2 -> N
# a[v1] + b[v2] + c[N]
# 2. 1 -> v2 -> v1 -> N
# a[v2] + c[v1] + b[N]
ans = min(a[v2] + c[v1] + b[N], a[v1] + b[v2] + c[N])
if ans < inf:
    print(ans)
else:
    print(-1)


