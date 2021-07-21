# import sys
# input = sys.stdin.readline

# n = int(input())
# board = [list(map(int,(input().split()))) for _ in range(n)]

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# ans = 0

# visited = [[0]*n for _ in range(n)]
# day = [[0]*n for _ in range(n)]

# def dfs(r, c, eat, cnt):
#     global ans    
#     # print(r, c, eat, cnt)    
#     for k in range(4):
#         nr = r + dr[k]
#         nc = c + dc[k]    
#         if 0 <= nr < n and 0 <= nc < n and eat < board[nr][nc] and visited[nr][nc] == 0:     
#             if day[nr][nc] < cnt+1:
#                 # print('eat', eat, board[nr][nc])                     
#                 visited[nr][nc] = 1 
#                 dfs(nr, nc, board[nr][nc], cnt + 1)                                
#                 visited[nr][nc] = 0
                       
#     if ans < cnt:
#         ans = cnt

# for i in range(n):
#     for j in range(n):
#         # print(i,j,board,visited)
#         dfs(i, j, board[i][j], 1)
#         day[i][j] = ans
# print(ans)




import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
board = [list(map(int,(input().split()))) for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
ans = 0
dp = [[0]*n for _ in range(n)]


def dfs(r, c, eat):
    global ans    
    if dp[r][c]:
        return dp[r][c]
    dp[r][c] = 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]    
        if 0 <= nr < n and 0 <= nc < n and eat < board[nr][nc]:                                 
            dp[r][c] = max(dp[r][c], dfs(nr, nc, board[nr][nc]) + 1)
                       
    if ans < dp[r][c]:
        ans = dp[r][c]

    return dp[r][c]

for i in range(n):
    for j in range(n):        
        dfs(i, j, board[i][j])
        
        
print(ans)
# print(answer)
