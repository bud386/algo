import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(population, cnt, i, j): # 인구수 총합, 연합에 들어있는 국가수, 시작국가 좌표
    union_country = [(i, j)] # 연합에 속한 국가들의 좌표들을 담을 리스트
    while q:
        r, c = q.popleft()
        for i in range(4):
            nextR = r + dr[i]
            nextC = c + dc[i]
            if 0 <= nextR < N and 0 <= nextC < N and visited[nextR][nextC] == 0 and L <= abs(board[r][c]-board[nextR][nextC]) <= R:
                visited[nextR][nextC] = 1        
                q.append((nextR, nextC))
                union_country.append((nextR,nextC))
                population += board[nextR][nextC]
                cnt += 1
    
    if cnt > 1: # 위 조건에 맞추어 방문한 국가가 2곳 이상이면 인구 이동 발생
        avg = population//cnt
        for country in union_country:
            board[country[0]][country[1]] = avg

q = deque()
ans = 0

while True:    
    visited = [[0]*N for _ in range(N)]
    union_num = 0 # 연합의 수

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                q.append((i, j))
                union_num += 1
                population = board[i][j]
                bfs(population, 1, i, j) # 인구수 총합, 연합에 들어있는 국가수, 시작국가 좌표

    if union_num == N*N:    # 모든 위치에 대해 각각 bfs이루어 진다면 인구 이동 끝 (각각의 국가가 하나의 연합)
        break
    else:
        ans += 1

print(ans)
    






# 문제 해석을 처음에 잘못해서 인구이동 횟수를 잘 못 세어주었다.
