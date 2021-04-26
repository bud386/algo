import sys
input = sys.stdin.readline 

dp0 = [1, 0, 1, 1, 2, 3]    # 0 ~ 5까지
dp1 =[0, 1, 1, 2, 3, 5]     # 0 ~ 5까지

for tc in range(int(input())):
    N = int(input())
    for i in range(len(dp0)-1, N+1):
        dp0.append(dp0[i]+dp0[i-1])
        dp1.append(dp1[i]+dp1[i-1])
    print(dp0[N], dp1[N])
    