import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 1
visited[r][c] = 1

def dfs(r, c, d):
    global ans 
    check = False
    for _ in range(4):
        nd = (d+3) % 4
        nr = r + dr[nd] 
        nc = c + dc[nd]
        
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:
            if visited[nr][nc] == 0:                
                ans += 1
                check = True
                visited[nr][nc] = 1
                dfs(nr, nc, nd) 
                return
        d = nd
    if check == False:
        nd = (d+2) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:
            dfs(nr, nc, d)

dfs(r, c, d)
print(ans)
