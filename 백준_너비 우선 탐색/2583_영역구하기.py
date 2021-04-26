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

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
# 영역의 수
count = 0
# 각 영역의 넓이 리스트
areas = []

def bfs(i,j):
    area = 1
    q.append((i,j))
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

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and board[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j)
            count +=1
areas.sort()
print(count)
print(*areas)


