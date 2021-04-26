import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    l = int(sys.stdin.readline())

    board = [[0 for _ in range(l)] for _ in range(l)]
    visited = [[0 for _ in range(l)] for _ in range(l)]
    q = deque()

    # 출발 지점과 도착지점
    for i in range(2):
        x, y = map(int, sys.stdin.readline().split())
        if i == 0:
            board[x][y] = 1
            # 출발 지점 q에 저장, 
            q.append((x, y, 1))
        else:
            board[x][y] = 2

                
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    # print(board)
    
    # while문 빠져나오기 위해
    flag = 0

    while q:
        now = q.popleft()
        # 시작지점이 도착지점과 같을떄
        if board[now[0]][now[1]] == 2:
            print(0)
            break
        
        for i in range(8):
            nextX = now[0] + dx[i]
            nextY = now[1] + dy[i]
            
            if 0 <= nextX < l and 0 <= nextY < l and visited[nextX][nextY] == 0:
                # 도착지점이면 while문 빠져나오게 flag = 1
                if board[nextX][nextY] == 2:
                    # print('boar=1', nextX, nextY)
                    # print(now[2])
                    # break
                    flag = 1
                elif board[nextX][nextY] == 0:
                    # print('board=0', nextX, nextY)
                    visited[nextX][nextY] = 1
                    q.append((nextX, nextY, now[2]+1))
        
        if flag == 1:
            print(now[2])
            break

    
