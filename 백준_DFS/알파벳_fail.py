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