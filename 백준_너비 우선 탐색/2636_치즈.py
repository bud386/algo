import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    global melted
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
                visited[nr][nc] = 1 
                if board[nr][nc] == 1:
                    board[nr][nc] = 'c'
                else:
                    q.append([nr, nc])

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'c':
                board[i][j] = 0
                cnt += 1            
    
    return cnt

q = deque()
time = 0
ans = 0
while True:    
    q.append([0, 0])
    visited = [[0]*m for _ in range(n)]
    melted_cnt = bfs() # 녹은 치즈 개수
    
    if melted_cnt == 0:
        print(time)
        print(ans)
        break
    else:
        time += 1
        ans = melted_cnt

    
    

