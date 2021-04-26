import sys
from collections import deque
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
del_node = int(input())

graph = [[] for _ in range(N)]
root = []
for i in range(N):
    if parents[i] != -1:
        graph[i].append(parents[i])
        graph[parents[i]].append(i)
    else:
        root.append(i)

visited = [0] * N

q = deque()

# root를 q에 넣어주고 방문 표시
for node in root:
    q.append(node)
    visited[node] = 1

visited[del_node] = 1
leaf_node = []

while q:
    now = q.popleft()
    # root와 지울 노드가 같을때
    if now == del_node:
        # root가 2개 이상일때
        if q:
            now = q.popleft()
        else:
            break
        
    cnt = 0
    for node in graph[now]:
        if visited[node] == 0:
            visited[node] = 1
            q.append(node)
        else:
            cnt += 1
    # 리프 노드이면 연결된 모든 노드를 이미 방문한 상태여야함.
    if cnt == len(graph[now]):
        leaf_node.append(now)

print(len(leaf_node))



