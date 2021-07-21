import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * N
dp[0] = 9
dp[1] = 17
dp[2] = 32

for i in range(3, N):
    dp[i] = dp[i-1]*2 -i

print(dp[N-1])