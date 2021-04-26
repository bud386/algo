from sys import stdin
n = int(input())

board = []

for i in range(n) :
    board.append(list(map(int, stdin.readline().strip())))


visited = [[0 for _ in range(n)] for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c) :
    
    visited[r][c] = 1
    
    sum = 1
    
    for i in range(4) :
        nextR = r+dr[i]
        nextC = c+dc[i]
        
        if 0<=nextR<n and 0<=nextC<n :
            if visited[nextR][nextC]==0 and board[nextR][nextC]==1 :
                sum+=dfs(nextR, nextC)

    return sum

ans = []

for i in range(n) :
    for j in range(n) :
        if board[i][j]==1 and visited[i][j]==0 :
            ans.append(dfs(i,j))

a.sort(ans)

print(len(ans))
for i in ans :
    print(i)