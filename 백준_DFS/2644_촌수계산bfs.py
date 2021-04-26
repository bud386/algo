import sys
from collections import deque

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (n+1)
que = deque([(a , 0)])
visited[a] = 1 # bfs할때 시작점 방문했다고 표시해줘야함
related = False

while que:
    now = que.popleft()

    if now[0] == b:
        related = True
        break

    for i in graph[now[0]]:
        if visited[i] == 0:
            visited[i] = 1 # 여기서 표시
            que.append((i, now[1] + 1))

if related:
    print(now[1])
else:
    print(-1)

