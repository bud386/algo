import sys
input = sys.stdin.readline 

dp = [0, 1, 2, 3, 5, 8]

N = int(input())
for i in range(5, N+1):
    dp.append(dp[i]+dp[i-1])

print(dp)
print(dp[N]%10007)
    

def make(i):
    print(i, dp)
    if i == n:
        return 1
    elif i > n:
        return 0

    if dp[i]:
        return dp[i]
    print(i)
    dp[i] = make(i+1) + make(i+2)
    print(dp, i,'#')
    return dp[i]

n = int(input())
dp = [0]*(n+1)
print(make(0), dp)