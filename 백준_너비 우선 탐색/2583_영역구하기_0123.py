# 최단경로 
# visitied는 보드판이 바뀌지 않아야할때?
# 
from collections import deque
import sys

# m(세로 = 행 = col = x) 
# n(가로 = 열 = r = y) 
# k(직사각형수)
m, n, k = map(int, sys.stdin.readline().split())


# 직사각형이 있는 좌표는 1로 표시
board = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[j][i] = 1
# print(board)

visited = [[0 for _ in range(n)] for _ in range(m)]

# 빈공간 좌표 저장
locations = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            locations.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
# 영역의 수
count = 0
# 각 영역의 넓이 리스트
areas = []

for location in locations:
    if visited[location[0]][location[1]] == 0:
        # 방문했다고 표시
        # 방문표시 안해주면 밑에서 bfs하면서 넓이 구할 때 한번씩 더셈
        visited[location[0]][location[1]] = 1
        q.append(location)
        area = 1
        while q:
            now = q.popleft()
            for i in range(4):
                nextX = now[1] + dx[i]
                nextY = now[0] + dy[i]
                if 0 <= nextX < n and 0 <= nextY < m and visited[nextY][nextX] == 0 and board[nextY][nextX] == 0:
                    q.append((nextY, nextX))
                    visited[nextY][nextX] =1
                    area += 1
        areas.append(area)
        count += 1

areas.sort()
print(count)
print(*areas)


