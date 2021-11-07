# 위상정렬
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
inDegree = [0] * (N+1) # 진입차수
inDegree[0] = -1
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    inDegree[b] += 1
    graph[a].append(b)

q = deque()

for i in range(1, N+1):
    if inDegree[i] == 0:
        q.append(i)

ans = []

while q:
    node = q.popleft()
    ans.append(node)
    for n_node in graph[node]:
        inDegree[n_node] -= 1
        if inDegree[n_node] == 0:
            q.append(n_node)
        
print(*ans)    


# dfs로 푸는 방법
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = []
visited = [0] * (N+1)
def dfs(node):    
    for n_node in graph[node]:
        if visited[n_node] == 0:
            visited[n_node] = 1
            dfs(n_node)
            ans.append(n_node)
    
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)

for i in range(1, N+1):
    if visited[i] == 0:
        ans.append(i)

print(*ans)

