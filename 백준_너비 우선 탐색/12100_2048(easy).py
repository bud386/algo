import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(board)
q = deque()

for i in range(N):
    for j in range(N):
        if board[i][j]:
            q.append([i, j, board[i][j]])
