import sys
input = sys.stdin.readline

board = [list(input().split()) for _ in range(5)]

dr = [1,-1, 0, 0]
dc = [0, 0, 1, -1]
ans = []

def dfs(r, c, num):
    if len(num) == 6:
        ans.append(num)
        return

    for i in range(4):
        nextR = r + dr[i]
        nextC = c + dc[i]
        
        if 0 <= nextR < 5 and 0 <= nextC < 5:
            dfs(nextR, nextC, num + board[nextR][nextC])
    
for r in range(5):
    for c in range(5):
        dfs(r, c, board[r][c])

print(len(set(ans)))
