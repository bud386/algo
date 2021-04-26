import sys
from collections import deque

n = int(sys.stdin.readline())

board = []
for _ in range(n):
    board.append(list(map(str, input())))
# print(board)

visited = [[0 for _ in range(n)] for _ in range(n)]

q = deque()

dc = [1, -1, 0, 0]
dr = [0, 0, 1, -1]

# 적록색약이 아닌 경우
count_color = 0
for i in range(n):
    for j in range(n):
        # 1. 'R'에 대한 bfs
        if visited[i][j] == 0 and board[i][j] == 'R':
            visited[i][j] = 1
            q.append((i, j))
            while q:
                now = q.popleft()
                
                for r in range(4):
                    nextC = now[0] + dc[r]
                    nextR = now[1] + dr[r]

                    if 0 <= nextC < n and 0 <= nextR < n and visited[nextC][nextR] == 0 and board[nextC][nextR] == 'R':
                        visited[nextC][nextR] = 1
                        q.append((nextC, nextR))
            count_color += 1
        # 2. 'G'에 대한 bfs
        elif visited[i][j] == 0 and board[i][j] == 'G':
            visited[i][j] = 1
            q.append((i, j))
            while q:
                now = q.popleft()
                
                for g in range(4):
                    nextC = now[0] + dc[g]
                    nextR = now[1] + dr[g]

                    if 0 <= nextC < n and 0 <= nextR < n and visited[nextC][nextR] == 0 and board[nextC][nextR] == 'G':
                        visited[nextC][nextR] = 1
                        q.append((nextC, nextR))
            count_color += 1
        # 3. 'B'에 대한 bfs
        elif visited[i][j] == 0 and board[i][j] == 'B':
            visited[i][j] = 1
            q.append((i, j))
            while q:
                now = q.popleft()
                
                for b in range(4):
                    nextC = now[0] + dc[b]
                    nextR = now[1] + dr[b]

                    if 0 <= nextC < n and 0 <= nextR < n and visited[nextC][nextR] == 0 and board[nextC][nextR] == 'B':
                        visited[nextC][nextR] = 1
                        q.append((nextC, nextR))
            count_color += 1

# 적록 색약인 경우
visited = [[0 for _ in range(n)] for _ in range(n)]

count_color_weakness = 0
for i in range(n):
    for j in range(n):
        # 1. 'R'과 'G'에 대한 bfs
        if visited[i][j] == 0 and (board[i][j] == 'R' or board[i][j] == 'G'):
            visited[i][j] = 1
            q.append((i, j))
            while q:
                now = q.popleft()
                
                for rg in range(4):
                    nextC = now[0] + dc[rg]
                    nextR = now[1] + dr[rg]

                    if 0 <= nextC < n and 0 <= nextR < n and visited[nextC][nextR] == 0 and (board[nextC][nextR] == 'R' or board[nextC][nextR] == 'G'):
                        visited[nextC][nextR] = 1
                        q.append((nextC, nextR))
            count_color_weakness += 1
        # 2. 'B'에 대한 bfs
        elif visited[i][j] == 0 and board[i][j] == 'B':
            visited[i][j] = 1
            q.append((i, j))
            while q:
                now = q.popleft()
                
                for bb in range(4):
                    nextC = now[0] + dc[bb]
                    nextR = now[1] + dr[bb]

                    if 0 <= nextC < n and 0 <= nextR < n and visited[nextC][nextR] == 0 and board[nextC][nextR] == 'B':
                        visited[nextC][nextR] = 1
                        q.append((nextC, nextR))
            count_color_weakness += 1

print(count_color, count_color_weakness)


# 오타 주의!