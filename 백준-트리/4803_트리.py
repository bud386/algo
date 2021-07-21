import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(node):
    global cycle
    if visited[node]:
        cycle = True
        return  # 여기 조건 있어야 시간 단축
    visited[node] = 1
    
    for i in graph[node]:
        if adj[node][i] == 0:
            adj[node][i] = 1
            adj[i][node] = 1
            dfs(i)

            
tc = 0 
while True:
    tc += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n+1)]
    adj = [[0] * (n+1) for _ in range(n+1)] # 인접 행렬
    visited = [0] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # print(graph)
    cnt = 0 
    for i in range(1, n+1):
        if visited[i] == 0:
            cycle = False
            dfs(i)
            if cycle == False:
                cnt += 1

    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')
