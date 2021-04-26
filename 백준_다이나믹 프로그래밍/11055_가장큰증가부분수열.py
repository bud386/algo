import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [i for i in arr]   # arr[0] ~ arr[i]까지의 가장 큰 증가부분수얄
for i in range(N):
    ans = arr[i]
    for j in range(i):  # arr[0] ~ arr[i]까지 확인
        if arr[i] > arr[j]:                    
            ans = max(ans, dp[i]+dp[j]) # 0~j까지 최대값 더하기
    dp[i] = ans


print(max(dp)) 
            
