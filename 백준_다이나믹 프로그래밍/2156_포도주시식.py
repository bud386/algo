import sys
input = sys.stdin.readline

N = int(input())
wine = [int(input()) for _ in range(N)]

if N <= 2:
    print(sum(wine))
else:
    dp = [0] * N
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0]+wine[2], wine[1]+wine[2], dp[1])

    # 4번째 와인부터 시작해서  
    # i번째 와인 까지 먹을때 최대값
    for i in range(3, N):
        dp[i] = max(
            wine[i] + wine[i-1] + dp[i-3],  # i번, i-1번 포도주 먹고 i-3번 포도주 안먹는 경우
            wine[i] + dp[i-2],  # i번 포도주만 먹고 i-1번 포도주 안먹는경우
            dp[i-1] # i번 포도주 안먹는경우
        )

    # print(dp)
    print(dp)
    print(dp[N-1])


# n = int(input())
# wine_list = [int(input()) for x in range(n)]
# print(wine_list)
# dp = [0]
# dp.append(wine_list[0])
# if(n > 1):
#     dp.append(wine_list[0] + wine_list[1])

# # 연속 3잔을 마시지 않아야 하므로
# # 1 : 이번 포도주를 먹고 이전 포도주를 먹지 않은 경우
# # 2 : 이번 포도주를 먹고 이전 포도주도 먹은 경우
# # 3 : 이번 포도주를 먹지 않아야 하는 경우
# # 위 세가지 경우를 고려하여 max

# for i in range(3, n + 1):
#     # wine_list는 0부터 시작하므로 i - 1로 해준다.
#     case_1 = wine_list[i - 1] + dp[i - 2]
#     case_2 = wine_list[i - 1] + wine_list[i - 2] + dp[i - 3]
#     case_3 = dp[i - 1]
#     max_value = max(case_1, case_2, case_3)
    
#     dp.append(max_value)
    
# print(dp)
# print(dp[n])