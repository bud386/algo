import sys
input = sys.stdin.readline
from collections import deque

N = int(input()) # 보드 크기
board = [[0]*N for _ in range(N)]
K = int(input()) # 사과 개수
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = -1

L = int(input()) # 방향 변환 횟수
time_directions = []
for _ in range(L):
    X, C  = input().split() # x초 뒤에 왼쪽 or 오른쪽
    time_directions.append([int(X), C])


# 북 동 남 서
# R(오른쪽 (d +1) % 4)
# L(왼쪽 (d + 3) & 4)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


q = deque()
r, c, d, time = 0, 0, 1, 0
q.append([r, c]) # r, c, d, time
board[r][c] = 1 # 뱀 표시
idx = 0 

while True:    

    if idx < L and time == time_directions[idx][0]:
        if time_directions[idx][1] == 'D':
            d = (d+1) % 4
        else:
            d = (d+3) % 4
        idx += 1

    r += dr[d]
    c += dc[d]
    if 0 <= r < N and 0 <= c < N:
        # 조건 1: 자기 꼬리를 물때
        if board[r][c] == 1:            
            print(time +1)
            break

        else:
            if board[r][c] != -1: # 사과 없는 경우
                tail_r, tail_c = q.popleft()
                board[tail_r][tail_c] = 0
            board[r][c] = 1
            q.append([r, c])
            time += 1
        
    # 조건 2: 벽을 만날때
    else:
        print(time+1)
        break
        

        
