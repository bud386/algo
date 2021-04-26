import sys
input = sys.stdin.readline
# from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

dr = [1, 0]
dc = [0, 1]
dp[0][0] = 1    

# 모든 칸에 대하여
for r in range(N):
    for c in range(N):
        if board[r][c] == 0:
            break
        for i in range(2):
            nr = r + dr[i]*board[r][c]
            nc = c + dc[i]*board[r][c]
            if 0 <= nr < N and 0 <= nc < N:
                dp[nr][nc] += dp[r][c]  # 다음 경로의 수는 현재 경로의 수 + 이전 경로의 수

print(dp[N-1][N-1])



# def dfs(r, c):
#     global cnt
#     for i in range(2):
#         nr = r + dr[i]*board[r][c]
#         nc = c + dc[i]*board[r][c]
#         if 0 <= nr < N and 0 <= nc < N:
#             dp[nr][nc] += dp[r][c]
#             if nr == N-1 and nc == N-1:
#                 # cnt += 1
#                 return 
#             dfs(nr, nc)
# dfs(0, 0)
# print(dp)
# print(dp[N-1][N-1])


# r = 0
# c = 0
# while True:
#     for i in range(2):
#         nr = r + dr[i]*board[r][c]
#         nc = c + dc[i]*board[r][c] 
#         board[]


# q = deque() 
# for i in range(2):
#         r = dr[i]*board[0][0]
#         c = dc[i]*board[0][0]
#         if 0 <= r < N and 0 <= c < N:
#             q.append([r, c])
#             dp[r][c] = 1

# while q:
#     r, c = q.popleft()
#     for i in range(2):
#         nr = r + dr[i]*board[r][c]
#         nc = c + dc[i]*board[r][c]
#         if 0 <= nr < N and 0 <= nc < N:
#             dp[nr][nc] += dp[r][c]
#             # visited[nr][nc] += 1
#             q.append([nr, nc])


# print(dp)