import sys
input = sys.stdin.readline

for tc in range(int(input())):
    
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    cnt = 0
    def dfs(node):
        global cnt
        visited[node] = 1
        for i in tree[node]:
            if visited[i] == 0:                
                cnt += 1
                dfs(i)

    dfs(1)
    print(cnt)