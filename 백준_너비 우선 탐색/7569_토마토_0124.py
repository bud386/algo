import sys
from collections import deque

# m - 가로, n - 세로, h - 상자 수
m, n, h = map(int, sys.stdin.readline().split())

board = []
# n세로길이의 상자를 h 만큼 쌓음
for _ in range(n * h):
    board.append(list(map(int, sys.stdin.readline().split())))

q = deque()

# 토마토가 들어있는 곳의 좌표를 q에 넣어서 시작
# bfs 전에 안 익은 토마토 카운트
cnt_zero_before = 0
for i in range(n * h):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j, 0))
        elif board[i][j] == 0:
            cnt_zero_before += 1

# print(q)
dr = [1, 0, -1, 0, 0, 0]
dc = [0, 1, 0, -1, n, -n]

# count = 0
while q:
    now = q.popleft()
    # print(now)
    for i in range(6):
        if i == 1: 
            if ((now[0] + dc[i]) % n) > (now[0] % n):
                nextC = now[0] + dc[i]
            else: # (1+1)%2 =0   <  1%2 =1
                nextC = now[0]
        elif i == 3:
            if ((now[0] + dc[i]) % n) < (now[0] % n):
                nextC = now[0] + dc[i]
            else:
                nextC = now[0]
        else:
            nextC = now[0] + dc[i] 
        # nextC = now[0] + dc[i] 
        nextR = now[1] + dr[i]

#        print(i, nextC, nextR)

        if 0 <= nextC < n*h and 0 <= nextR < m and board[nextC][nextR] == 0:
            board[nextC][nextR] = 1
            q.append((nextC, nextR, now[2]+1))
            # count = now[2] + 1

# print(board)

# bfs 하고나서 안익은 토마토 카운트
cnt_zero = 0
for i in range(n * h):
    for j in range(m):
        if board[i][j] == 0:
            cnt_zero += 1
            
# 처음에 안익은 토마토가 없으면
if cnt_zero_before == 0:
    print(0)
# bfs하고 안익은 토마토가 있으면
elif cnt_zero > 0:
    print(-1)
else:
    print(now[2])
    # print(count)

####
# 첫번째 박스의 마지막 행이 두번째 박스의 첫째 행과 연결되면서 틀림!!.
# 3차원 배열로 해결할것!!
### 반례
# 2 2 2

# -1 -1
# 1 -1

# 0 -1
# -1 -1

# 그래도 위에 처럼 경우 나눠서 어거지로 하면 되긴함



# 보드 생성할때 아래처럼 만듬;; --> n*h만 하면됨
#  for _ in range(n * h):
#     for _ in range(m):
#         board.append(list(map(int, sys.stdin.readline().split())))

# q에서 맨뒤에 0 값 추가해서 하면 따로 for문이나 count 변수 안쓰고 bfs 한번 할때마다 count를 셀 수 있음.

# # 처음에 안익은 토마토가 없으면
# if cnt_zero_before == 0:
#     print(0)
# 위에거 안해줘도딤
# 마지막 now[2] 에서 어차피 0찍힘