import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [arr[i] for i in range(N)]

for i in range(1, n): 
    dp[i] = max(dp[i], dp[i - 1] + arr[i])

print(max(dp))


    # N = int(input())
# arr = list(map(int, input().split()))
# dp = [arr[i] for i in range(N)]
# i = 0
# while i < N:
#     # print('zz',i)
#     total = arr[i]
#     end = i
#     for j in range(i+1, N):
#         total += arr[j]
#         if total > dp[i]:
#             dp[i] = total
#             end = j
                
#     while end > i:
#         dp[i+1] = dp[i] - arr[i]  
#         i += 1        
#     i += 1
    
# print(dp)
# print(max(dp))

