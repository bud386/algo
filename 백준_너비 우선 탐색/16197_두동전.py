import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input().strip()))

coin_a = deque()
coin_b = deque()
coin_type = True
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            if coin_type:
                coin_a.append([i, j, 0, 'a'])
                coin_type = False
            else:
                coin_b.append([i, j, 0, 'b'])
            
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    while coin_a or coin_b:
        a_r, a_c, a_cnt, a_coin_type = coin_a.popleft()
        b_r, b_c, b_cnt, b_coin_type = coin_b.popleft()
        for i in range(4):
            a_nr = a_r + dr[i]
            a_nc = a_c + dc[i]
            b_nr = b_r + dr[i]
            b_nc = b_c + dc[i]
            



print(board)