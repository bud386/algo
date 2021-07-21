import sys
input = sys.stdin.readline

N = int(input())
cost = list(map(int, input().split()))
dp = [0] * N
dp[0] = cost[0]
dp[1] = max(cost[0]*2, cost[1])

for i in range(2, N):
    dp[i] = cost[i]
    for j in range(i):
        # print(dp[i-j-1]+cost[j], cost[j], dp[i-j-1])
        dp[i] = max(dp[i-j-1] + cost[j], dp[i])
        
# print(dp)
print(dp[N-1])

