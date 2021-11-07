import sys
from collections import deque
inf = sys.maxsize

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(M)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

q = deque()
q.append([0, 0, board[0][0]])

min_cost = [[inf] * N for _ in range(M)]
min_cost[0][0] = 0


while q:
    r, c, cost = q.popleft()
    if min_cost[r][c] < cost:
        continue
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N:
            total_cost = cost + board[nr][nc]
            if min_cost[nr][nc] > total_cost:
                min_cost[nr][nc] = total_cost
                q.append([nr, nc, total_cost])
print(min_cost[N-1][M-1])