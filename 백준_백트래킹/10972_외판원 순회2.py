import sys
input = sys.stdin.readline
inf = sys.maxsize

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = inf

def dfs(now, weight, start):
    global ans
    if weight >= ans:
        return

    if sum(visited) == N: 
        if board[now][start]:
            ans = min(ans,weight + board[now][start])
        return

    for end in range(N):
        if board[now][end] and visited[end] == 0:
            visited[end] = 1
            dfs(end, weight + board[now][end], start)
            visited[end] = 0

visited = [0] * N
visited[0] = 1                
dfs(0, 0, 0)
print(ans)