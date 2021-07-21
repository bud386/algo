import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*i for i in range(1, N+1)]
dp[0][0] = board[0][0]

for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + board[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + board[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + board[i][j]
print(max(dp[N-1]))