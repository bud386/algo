import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
forest = [list(input().strip()) for _ in range(R)]

water_q = deque()
S_q = deque() # 고슴도치

for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            water_q.append((i, j))
        if forest[i][j] == 'S':
            S_q.append([i, j, 0])

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

while water_q or S_q:
    # 물 웅덩이 채우기
    if water_q:
        for _ in range(len(water_q)): # 처음에는 물웅덩이 수만큼 반복, 이후에는 방문한 위치만큼 반복
            now = water_q.popleft()
            for i in range(4):
                r = now[0] + dr[i]
                c = now[1] + dc[i]
                if 0 <= r < R and 0 <= c < C and forest[r][c] == '.':
                    forest[r][c] = '*'
                    water_q.append((r,c))
    
    # 고슴도치 이동
    if S_q:
        for _ in range(len(S_q)): # 고슴도치가 방문한 위치만큼 반복
            now = S_q.popleft()
            now[2] += 1 # 방문 순서 카운트
            for i in range(4):
                r = now[0] + dr[i]
                c = now[1] + dc[i]
                if 0 <= r < R and 0 <= c < C:
                    if forest[r][c] == 'D':
                        print(now[2]) # 정답 출력
                        exit()
                    elif forest[r][c] == '.':
                        forest[r][c] = now[2] # 방문한 순서 표시
                        S_q.append([r, c, now[2]])        

print('KAKTUS')
















# 물도 함께 비어있는 칸으로 확장되고 고슴도치 보다 먼저 움직여야 한다.
# 물웅덩이가 여러개 있을때 모든 물웅덩이에 대해 반복하여 한번에 움직여야 한다는 것이 핵심이다.

