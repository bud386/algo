import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]

for i in range(3):
    dp[0][i] = cost[0][i]   # 첫번째 집 최솟값 입력

for i in range(1, N):
    for j in range(3):
        # 이전 집에서 j번쨰 색깔을 빼고 더한것 중 최솟값
        if j == 0:
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + cost[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + cost[i][j]
        else:
            dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + cost[i][j]

print(min(dp[N-1]))