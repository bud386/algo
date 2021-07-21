import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append([0,0])
    visited = [[0]*m for _ in range(n)]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr <  n and 0 <= nc < m and visited[nr][nc] == 0:
                if board[nr][nc] == 0: # 빈칸일때
                    visited[nr][nc] = 1                
                    q.append([nr, nc])
                else: # 가장자리에 있는 치즈일때
                    board[nr][nc] += 1  # 공기에 접촉면 더하기
    
    melted = False # 녹은 치즈가 있는지 판단
    for i in range(n):
        for j in range(m):       
            if board[i][j] >= 3: # 가장자리이면서 접촉면이 2변이상
                board[i][j] = 0 # 녹이기
                melted = True
            elif board[i][j] == 2: # 가장자리이면서 접촉면이 1변뿐일때
                board[i][j] = 1
    return melted

ans = 0
while True:
    if bfs() == False: # 녹은 치즈가 없다면
        break
    ans += 1
print(ans)