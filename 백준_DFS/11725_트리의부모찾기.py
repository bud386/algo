import sys
from collections import deque
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0] * (N+1)
visited = [0] * (N+1)

def dfs(s):
    visited[s] = 1
    for node in graph[s]:
        if visited[node] == 0:
            # dfs하는 노드의 부모는 s
            ans[node] = s
            dfs(node)

dfs(1)
for i in range(2, N+1):
    print(ans[i])

# print()


# ans2 = [0] * (N+1)
# visit = [0] * (N+1)
# q = deque([1])
# visit[1] = 1
# ans = 2

# while q:
#     now = q.popleft()
#     for node in graph[now]:
#         if visit[node] == 0:
#             visit[node] = 1
#             ans2[node] = now
#             q.append(node)

# for i in range(2, N+1):
#     print(ans2[i])

