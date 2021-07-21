import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# prim 알고리즘
key = [9999999] * (V+1)   # 각 node 연결하는 최소 비용을 저장할 배열
visited = [0] * (V+1) # 최소비용으로 연결된 node 체크

# 1번 node부터 시작
key[1] = 0
visited[1] = 1
ans = 0 # 모든 node 연결했을때의 최소비용

for _ in range(V):
    # 현재 갈수있는 node에서 최소 비용이 드는 노드 탐색
    minK = 9999999
    u = 1
    for i in range(1, V+1):
        if visited[i] == 0 and minK > key[i]:
            u = i
            minK = key[i]

    ans += key[u]
    visited[u] = 1

    for v, w in graph[u]:   # u번째 노드와 연결된 노드들과 비용(w)에 대하여
        # 최소 연결 비용 탐색
        if visited[v] == 0 and key[v] > w:
            key[v] = w

print(ans)