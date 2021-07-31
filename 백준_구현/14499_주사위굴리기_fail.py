import sys
input = sys.stdin.readline

N, M, r, c, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(int, input().split()))

dice = [0] * 7

# 동 서 북 남
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

for d in directions:
    r += dr[d-1]
    c += dc[d-1]
    if 0 <= r < N and 0 <= c < M:
        if d == 1:
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
        elif d == 2:
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
        elif d == 3:
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
        else:
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
        
        if board[r][c]:
            dice[6] = board[r][c]
            board[r][c] = 0
        else:
            board[r][c] = dice[6]

        print(dice[1])
    else:
        r -= dr[d-1]
        c -= dc[d-1]
    
