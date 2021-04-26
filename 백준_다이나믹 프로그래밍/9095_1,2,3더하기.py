import sys
input = sys.stdin.readline 
arr = [1, 2, 3]

for tc in range(int(input())):
    n = int(input())
    total = 0
    cnt = 0
    
    def check(i):
        global total, cnt        
        if total > n:
            return
        if total == n:
            cnt += 1
            return
        else:
            for i in range(3):
                total += arr[i]
                check(i)
                total -= arr[i]
    check(0)
    print(cnt)

# DP 풀이
dp = [1, 2, 4]
for i in range(3, 10):
    dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
for tc in range(int(input)):
    n = int(input())
    print(dp[n - 1])
