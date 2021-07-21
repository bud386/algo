import sys
from collections import deque
import copy
input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

virus_cnt = 0   # 처음 바이러스의 개수
virus_loc = []  # 바이러스의 위치
empty_cnt = 0   # 빈칸의 개수
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus_cnt += 1
            virus_loc.append([i, j, 0]) # 좌표와, 시작 시간 
        elif board[i][j] == 0:
            empty_cnt += 1


def bfs(q, visited):
    global ans
    # 비어있는 칸에 몇초 걸려서 감염시키는지
    while q:
        r, c, time = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1:                
                if visited[nr][nc] > time + 1:                    
                    visited[nr][nc] = time + 1
                    q.append([nr, nc, time + 1])

    
    spread_cnt = 0 # 몇칸 감염시켰는지
    max_time = 0 # 빈칸을 감염시키는데 걸린 시간

    for i in range(n):
        for j in range(n):
            if visited[i][j] != inf and board[i][j] == 0:
                if visited[i][j] > max_time:
                    max_time = visited[i][j]
                spread_cnt += 1

    # 만약 감염시킨 칸의 개수가 처음 빈칸의 개수와 같을때
    if spread_cnt == empty_cnt:
        if max_time < ans:
            ans = max_time   
        return

def combi(cnt, start):    
    global virus_cnt, m
    # 바이러스를 m개 뽑는 조합
    if cnt == m:         
        visited = [[inf]*n for _ in range(n)] # 시작점으로부터 각 좌표까지의 시간
        # 시작 좌표는 0
        for loc in pick:
            visited[loc[0]][loc[1]] = 0
        q = copy.deepcopy(pick)
        bfs(q, visited)
        return    
    for i in range(start, virus_cnt):                
        pick.append(virus_loc[i])
        combi(cnt + 1, i + 1)            
        pick.pop()

pick = deque()
ans = inf
combi(0, 0)
if ans == inf:
    print(-1)
else:
    print(ans)           

