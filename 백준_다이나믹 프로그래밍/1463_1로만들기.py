import sys
input = sys.stdin.readline 
n = int(input())
dp = [0, 0, 1, 1, 2, 3, 2]  # 0 ~ 6까지 최솟값

for i in range(7, n+1): # 7부터 n까지의 경우
    ans = []
    if i % 3 == 0:  
        ans.append(1+dp[i//3])
    if i % 2 == 0:  
        ans.append(1+dp[i//2])
    ans.append(1+dp[i-1]) # -1 했을 때
    
    dp.append(min(ans)) # 3개중에서 가장 작은 값

print(dp[n])


# bfs로 풀기 가능