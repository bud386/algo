import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
 
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    visited[r][c] = 1
    global cnt
    for i in range(4):
        nextR = r + dr[i]
        nextC = c + dc[i]
        if 0 <= nextR < N and 0 <= nextC < M and board[nextR][nextC] == 1 and visited[nextR][nextC] == 0:
            cnt += 1
            dfs(nextR, nextC)

ans = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 1 and visited[r][c] == 0:
            cnt = 1
            dfs(r,c)
            ans.append(cnt)
            

print(max(ans))

