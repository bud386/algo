import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# visited = {}
# for i in board:
#     for alpha in i:
#         visited[alpha] = 0
# visited[board[0][0]] = 1
ans = 0

visited = [0] * 26
visited[ord(board[0][0]) - 65] = 1

def dfs(r, c, cnt):
    global ans    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < n and 0 <= nc < m and visited[ord(board[nr][nc]) - 65] == 0:
            visited[ord(board[nr][nc]) - 65] = 1            
            dfs(nr, nc, cnt + 1)
            visited[ord(board[nr][nc]) - 65] = 0                       
        # if 0 <= nr < n and 0 <= nc < m and visited[board[nr][nc]] == 0:
        #     visited[board[nr][nc]] = 1            
        #     dfs(nr, nc, cnt + 1)
        #     visited[board[nr][nc]] = 0                        
    if ans < cnt:
        ans = cnt

dfs(0, 0, 1)
print(ans)



    

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

Board = [list(map(str, input().strip())) for _ in range(N)]

def to_num(x, y):
    return ord(Board[x][y]) - ord('A')	


visited = [0] * 26
visited[to_num(0,0)] = 1
answer = 1


def DFS(currX, currY, depth):
	global answer
	
	dx, dy = [1,-1,0,0], [0,0,1,-1]
	
	for i in range(4):
		xx, yy = currX + dx[i], currY + dy[i]
		
		if xx >=N or yy >= M or xx < 0 or yy < 0:
			continue
			
		if visited[to_num(xx,yy)] != 1:
			visited[to_num(xx,yy)] = 1
			DFS(xx, yy, depth+1)
			visited[to_num(xx,yy)] = 0
		
	answer = max(answer, depth)
	
DFS(0,0,1)
print(answer)


# https://www.acmicpc.net/board/view/33029
# https://www.acmicpc.net/board/view/32991
# https://www.acmicpc.net/board/view/56580 - Python에서 dict와 list의 속도 차이