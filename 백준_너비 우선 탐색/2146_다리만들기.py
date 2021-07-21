import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N 
for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

q = deque()

def numbering_bfs(num):
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and board[nr][nc] == 1:
                visited[nr][nc] = 1
                board[nr][nc] = num
                q.append([nr,nc])

num = 2
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            q.append([i, j])
            visited[i][j] = 1
            board[i][j] = num
            numbering_bfs(num)
            num += 1



def bfs(island):
    global ans
    while q:
        r, c, cnt = q.popleft()

        if cnt == ans:
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]            
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc]:
                if board[nr][nc] != island:
                    if ans > cnt:
                        ans = cnt
                        return

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and board[nr][nc] == 0:
                visited[nr][nc] = 1                
                q.append([nr, nc, cnt+1])

ans = 99999

for i in range(N):
    for j in range(N):
        if board[i][j]:
            visited = [[0] * N for _ in range(N)]
            island = board[i][j]
            q = deque()       
            q.append([i, j, 0])
            visited[i][j] = 1     
            bfs(island)
            

print(ans)

