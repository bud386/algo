import sys
from collections import deque

# 동서남북, 대각선 4경우
dr = [0, 1, 0, -1, 1, 1, -1, -1 ]
dc = [1, 0, -1, 0, 1, -1, 1, -1 ]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    while q:
        now = q.popleft()
        for i in range(8):
            nextR = now[0] + dr[i]
            nextC = now[1] + dc[i]
            if 0 <= nextR < h and 0 <= nextC < w and board[nextR][nextC] == 1:
                board[nextR][nextC] = 2
                q.append((nextR,nextC))
            
while True:
    # 맵의 크기
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    # 섬의 위치 입력
    board = []
    for i in range(h):
            board.append(list(map(int, sys.stdin.readline().split())))

    count= 0
    for i in range(h):
            for j in range(w):
                if board[i][j] == 1:
                    bfs(i,j)
                    count += 1

    print(count)

