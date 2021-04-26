import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
cnt_list = [[0]*M for _ in range(N)]    # 각 빙산 주변의 바닷물 개수를 담은 리스트
# print()
# for i in range(N):
#     print(*board[i])
# print()
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
year = 1    # 최소시간 기록

while True:
    group = 0       # 빙산 그룹의 수
    bing_cnt = 0        # 빙산의 수

    for i in range(1, N-1):
        for j in range(1, M-1):
            if board[i][j] != 0:
                cnt = 0     # 주변의 바닷물 개수
                bing_cnt += 1
                for k in range(4):
                    r = i + dr[k]
                    c = j + dc[k]
                    if board[r][c] == 0:
                        cnt += 1
                cnt_list[i][j] = cnt    # 각 빙산 주변의 바닷물 개수를 담은 리스트

    # 빙산이 하나 있다면 분리도 안되고 다 녹아 없어짐 
    if bing_cnt == 1:
        print(0)
        break

    # 빙산이 녹는 과정
    for i in range(1, N-1):
        for j in range(1, M-1):
            if board[i][j] - cnt_list[i][j] >= 0:
                board[i][j] -= cnt_list[i][j]
            else:
                board[i][j] = 0
    

    visited = [[0]*M for _ in range(N)]
    q = deque()

    for i in range(1, N-1):
        for j in range(1, M-1):
            if visited[i][j] == 0 and board[i][j] != 0:
                q.append((i,j))
                visited[i][j] = 1
                
                while q:
                    r, c = q.popleft()
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and board[nr][nc] != 0:
                            q.append((nr,nc))
                            visited[nr][nc] = 1
                group += 1

    if group >= 2:
        print(year)
        break
    year += 1

                    
                

