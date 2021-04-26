import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c, k):
    visited[r][c] = 1
    for i in range(4):
        nextR = r + dr[i]
        nextC = c + dc[i]
        if  0 <= nextR < n and 0 <= nextC < n and visited[nextR][nextC] == 0 and board[nextR][nextC] > k:
            dfs(nextR, nextC, k)

# max_h = 0
# for h in board:
#     if max(h) > max_h:
#         max_h = max(h)

ans = []
for k in range(101):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for r in range(n):
        for c in range(n):
            if visited[r][c] == 0 and board[r][c] > k:
                dfs(r, c, k)
                cnt += 1
    ans.append(cnt)

print(max(ans))

