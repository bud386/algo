import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
baby_shark = deque()
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            baby_shark.append([i, j, 2, 0])
            board[i][j] = 0

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
ans = 0
eaten = 0   # 먹은 물고기 수
check = [[0]*N for _ in range(N)]
# for _ in range(10)
while True:
    visited = [[0]*N for _ in range(N)]
    eatable = []
    min_cnt = 9999
    flag = False
    while baby_shark:
        # print(baby_shark)
        x, y, size, cnt = baby_shark.popleft()
        # print(x,y,size,cnt)
        visited[x][y] = 1
        for i in range(4):
            r = x + dr[i]
            c = y + dc[i]
            if 0 <= r < N and 0 <= c < N and visited[r][c] == 0:
                if board[r][c] == 0 or board[r][c] == size:
                    visited[r][c] = 1
                    baby_shark.append([r, c, size, cnt + 1])
                elif board[r][c] != 0:
                    if board[r][c] < size:
                        board[r][c] = 0
                        eaten += 1
                        if eaten == size:
                            size += 1
                            eaten = 0
                        baby_shark = deque([[r, c, size, cnt + 1]])
                        flag = True
                        ans = cnt + 1
                        print((r,c), "size:", size, cnt + 1)
                        check[r][c] = cnt + 1
                        if cnt + 1 == 10:
                            for k in range(N):
                                print(*check[k])
                            print()
                            for k in range(N):
                                print(*board[k])
                                
                        break
        if flag:
            break
    if not baby_shark:
        break
                      # min_cnt = min(min_cnt, cnt+1)
print(ans)                        # eatable.append([r, c, cnt])
for i in range(N):
    print(*check[i])






# 반례
# 6
# 5 4 3 2 3 4
# 4 3 2 3 4 5
# 3 2 9 5 6 6
# 2 1 2 3 4 5
# 3 2 1 6 5 4
# 6 6 6 6 6 6
# (3, 1) size: 2 2
# (4, 2) size: 3 4
# (3, 2) size: 3 5
# (1, 2) size: 3 7
# (0, 3) size: 4 9
# (0, 2) size: 4 10
# 0 0 10 9 0 0
# 0 0 7 0 0 0
# 0 0 0 0 0 0
# 0 2 5 0 0 0
# 0 0 4 0 0 0
# 0 0 0 0 0 0

# 5 4 0 0 3 4
# 4 3 0 3 4 5
# 3 2 0 5 6 6
# 2 0 0 3 4 5
# 3 2 0 6 5 4
# 6 6 6 6 6 6
# (1, 1) size: 4 12
# (2, 1) size: 4 13
# (2, 0) size: 5 14
# (1, 0) size: 5 15
# (0, 1) size: 5 17
# (0, 4) size: 5 20
# (0, 5) size: 5 21
# (1, 4) size: 6 23
# (1, 3) size: 6 24
# (2, 3) size: 6 25
# (3, 3) size: 6 26
# (3, 4) size: 6 27
# (3, 5) size: 6 28
# (4, 5) size: 7 29
# (4, 4) size: 7 30
# (4, 3) size: 7 31
# (5, 3) size: 7 32
# (5, 2) size: 7 33
# (5, 1) size: 7 34
# (4, 1) size: 7 35
# (4, 0) size: 8 36
# (3, 0) size: 8 37
# (5, 0) size: 8 39
# (5, 4) size: 8 43
# (5, 5) size: 8 44
# (2, 5) size: 8 47
# (1, 5) size: 8 48
# (2, 4) size: 8 50
# (0, 0) size: 9 56
# 56
# 56 17 10 9 20 21
# 15 12 7 24 23 48
# 14 13 0 25 50 47
# 37 2 5 26 27 28
# 36 35 4 31 30 29
# 39 34 33 32 43 44