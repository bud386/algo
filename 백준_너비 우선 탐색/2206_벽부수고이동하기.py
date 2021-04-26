import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))

# wall[(0,0)] ---> 벽이 하나도 없을때를 위해서 이렇게 해도됨
walls = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            walls.append((i,j))
ans =[]

# 벽이 하나라도 있는경우
if walls:
    # 모든 벽의 좌표에 대하여(모든 벽에 대해서 각각 허무는 경우 bfs)
    for wall in walls:
        
        # 벽 허물기
        board[wall[0]][wall[1]] = 0
        visited = [[0 for _ in range(m)] for _ in range(n)]

        # q를 초기화 하고 시작지점 설정
        q = deque()
        q.append((0,0,2))

        while q: 
            now = q.popleft()
            # print(now)
            for i in range(4):
                nextX = now[0] + dx[i]
                nextY = now[1] + dy[i] 
                if nextX == n-1 and nextY == m-1:
                    ans.append(now[2])
                    break
                if 0 <= nextX < n and 0 <= nextY < m and visited[nextX][nextY] == 0 and board[nextX][nextY] == 0:
                    q.append((nextX, nextY, now[2]+1))
                    visited[nextX][nextY] = 1
        
        # bfs 끝나면 다시 벽 세우기
        board[wall[0]][wall[1]] = 1

# 벽이 없는 경우
else:
    q = deque()
    q.append((0,0,2))
    while q: 
        now = q.popleft()
            # print(now)
        for i in range(4):
            nextX = now[0] + dx[i]
            nextY = now[1] + dy[i] 
            if nextX == n-1 and nextY == m-1:
                ans.append(now[2])
                break
            if 0 <= nextX < n and 0 <= nextY < m and visited[nextX][nextY] == 0 and board[nextX][nextY] == 0:
                q.append((nextX, nextY, now[2]+1))
                visited[nextX][nextY] = 1

if ans:
    print(min(ans))
else:
    print(-1)