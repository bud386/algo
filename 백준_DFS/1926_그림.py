import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

q = deque()
picture_cnt = 0
picture_area = [0]

for r in range(n):
    for c in range(m):
        if board[r][c] == 1 and visited[r][c] == 0:
            q.append([r, c])
            visited[r][c] = 1
            area = 1
            while q:
                now = q.popleft()
                for k in range(4):
                    nextR = now[0] + dr[k]
                    nextC = now[1] + dc[k]
                    if 0 <= nextR < n and  0 <= nextC < m and board[nextR][nextC] == 1 and visited[nextR][nextC] == 0:
                        visited[nextR][nextC] = 1
                        q.append([nextR, nextC])
                        area += 1
            picture_area.append(area)
            picture_cnt += 1

print(picture_cnt)
print(max(picture_area))
