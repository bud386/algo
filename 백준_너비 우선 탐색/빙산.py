import sys
from collections import deque
import copy
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
que = []
for i in range(1, N-1):
    for j in range(1, M-1):
        if board[i][j] != 0:
            que.append([i, j, board[i][j]]) # 빙산의 좌표, 높이

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
year = 1    # 최소시간 기록
bing_cnt = len(que)        # 처음 빙산의 수

while True:
    group = 0       # 빙산 그룹의 수
    bing_cnt_after = 0  # 다 녹은 빙산의 수
    
    # 주변 바닷물 개수 세고 높이 저장하기
    for i in range(bing_cnt):
        cnt = 0     # 주변의 바닷물 개수
        for k in range(4):
            r = que[i][0] + dr[k]
            c = que[i][1] + dc[k]
            if board[r][c] == 0: # 바닷물이라면
                cnt += 1
        if que[i][2] - cnt > 0:     # 빙산의 높이에서 바닷물 개수 빼줌
            que[i][2] -= cnt
        else:
            que[i][2] = 0
            bing_cnt_after += 1     # 다 녹은 빙산의 수 +
    
    # 빙산이 하나 있다면 분리도 안되고 다 녹아 없어짐 
    if bing_cnt - bing_cnt_after <= 1:
        print(0)
        break
    
    
    # 빙산의 높이 재설정
    for i in range(bing_cnt):
        board[que[i][0]][que[i][1]] = que[i][2]     
    

    visited = [[0]*M for _ in range(N)]
    q = []
    for i in range(bing_cnt):
        if visited[que[i][0]][que[i][1]] == 0 and que[i][2] != 0:   # 빙산의 높이가 0이 아닐때
            q.append([que[i][0], que[i][1]])
            visited[que[i][0]][que[i][1]] = 1
            while q:
                r, c = q.pop()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and board[nr][nc] != 0:
                        q.append((nr,nc))
                        visited[nr][nc] = 1
            group += 1
            if group >= 2:
                print(year)
                exit()
    year += 1





# deque는 pop(index가 안되나?)